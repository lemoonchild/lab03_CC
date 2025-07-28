import sys
import time
import requests
import json
import os
from antlr4 import *
from TerraformSubsetLexer import TerraformSubsetLexer
from TerraformSubsetParser import TerraformSubsetParser
from TerraformSubsetListener import TerraformSubsetListener

class TerraformApplyListener(TerraformSubsetListener):
  def __init__(self):
    self.variables = {}
    self.provider_token_expr = None  # store raw expression (e.g., var.token)
    self.droplet_config = {}
    self.destroy_mode = False

  def enterVariable(self, ctx):
    var_name = ctx.STRING().getText().strip('"')
    for kv in ctx.body().keyValue():
      key = kv.IDENTIFIER().getText()
      if key == "default":
        value = kv.expr().getText().strip('"')
        self.variables[var_name] = value
        print(f"[var] {var_name} = {value}")

  def enterProvider(self, ctx):
    provider_name = ctx.STRING().getText().strip('"')
    if provider_name != "digitalocean":
      raise Exception("Only 'digitalocean' provider is supported.")

    for kv in ctx.body().keyValue():
      key = kv.IDENTIFIER().getText()
      expr = kv.expr().getText()
      if key == "token":
        self.provider_token_expr = expr  # store raw expr for now

  def enterResource(self, ctx):
    type_ = ctx.STRING(0).getText().strip('"')
    name = ctx.STRING(1).getText().strip('"')
    if type_ != "digitalocean_droplet":
      return

    for kv in ctx.body().keyValue():
      key = kv.IDENTIFIER().getText()
      val = kv.expr().getText().strip('"')
      self.droplet_config[key] = val

  def enterDestroy(self, ctx):
    self.destroy_mode = True
    print("[destroy] Destroy mode activated")

  def resolve_token(self):
    if not self.provider_token_expr:
      raise Exception("No token specified in provider block.")
    if self.provider_token_expr.startswith("var."):
      var_name = self.provider_token_expr.split(".")[1]
      if var_name in self.variables:
        return self.variables[var_name]
      else:
        raise Exception(f"Undefined variable '{var_name}' used in provider block.")
    return self.provider_token_expr.strip('"')

def create_state_file(droplet_name, droplet_id, droplet_ip):
  """Create or update terraform.tfstate file with droplet information"""
  state_data = {
    "version": 4,
    "terraform_version": "1.0.0",
    "serial": 1,
    "lineage": "custom-terraform-subset",
    "outputs": {},
    "resources": [
      {
        "mode": "managed",
        "type": "digitalocean_droplet",
        "name": "web",
        "provider": "provider[\"registry.terraform.io/digitalocean/digitalocean\"]",
        "instances": [
          {
            "schema_version": 1,
            "attributes": {
              "id": str(droplet_id),
              "name": droplet_name,
              "ipv4_address": droplet_ip,
              "status": "active"
            }
          }
        ]
      }
    ]
  }
  
  with open("terraform.tfstate", "w") as f:
    json.dump(state_data, f, indent=2)
  print(f"[+] State file created: terraform.tfstate")

def read_state_file():
  """Read droplet ID and IP from terraform.tfstate file"""
  if not os.path.exists("terraform.tfstate"):
    print("[!] No terraform.tfstate file found. Cannot destroy resources.")
    return None, None, None
  
  try:
    with open("terraform.tfstate", "r") as f:
      state_data = json.load(f)
    
    # Find digitalocean_droplet resource
    for resource in state_data.get("resources", []):
      if (resource.get("type") == "digitalocean_droplet" and 
          resource.get("name") == "web"):
        instance = resource["instances"][0]
        attributes = instance["attributes"]
        droplet_id = attributes["id"]
        droplet_name = attributes["name"]
        droplet_ip = attributes.get("ipv4_address", "unknown")
        print(f"[*] Found droplet in state: {droplet_name} (ID: {droplet_id}, IP: {droplet_ip})")
        return droplet_id, droplet_name, droplet_ip
    
    print("[!] No digitalocean_droplet resource found in state file")
    return None, None, None
    
  except Exception as e:
    print(f"[!] Error reading state file: {e}")
    return None, None, None

def delete_state_file():
  """Delete the terraform.tfstate file after successful destroy"""
  if os.path.exists("terraform.tfstate"):
    os.remove("terraform.tfstate")
    print("[+] State file removed: terraform.tfstate")

def create_droplet(api_token, config):
  url = "https://api.digitalocean.com/v2/droplets"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_token}"
  }

  payload = {
    "name": config["name"],
    "region": config["region"],
    "size": config["size"],
    "image": config["image"],
    "ssh_keys": [],
    "backups": False,
    "ipv6": False,
    "user_data": None,
    "private_networking": None,
    "volumes": None,
    "tags": []
  }

  print("[*] Creating droplet...")
  response = requests.post(url, headers=headers, json=payload)
  response.raise_for_status()
  droplet = response.json()["droplet"]
  droplet_id = droplet["id"]
  print(f"[+] Droplet created with ID: {droplet_id}")

  print("[*] Waiting for droplet to become active and assigned an IP...")
  while True:
    resp = requests.get(f"https://api.digitalocean.com/v2/droplets/{droplet_id}", headers=headers)
    droplet_info = resp.json()["droplet"]
    networks = droplet_info["networks"]["v4"]
    public_ips = [n["ip_address"] for n in networks if n["type"] == "public"]
    if public_ips:
      droplet_ip = public_ips[0]
      # Create state file with droplet information
      create_state_file(config["name"], droplet_id, droplet_ip)
      return droplet_id, droplet_ip
    time.sleep(5)

def destroy_droplet(api_token):
  """Destroy a droplet using ID from state file"""
  # Read droplet info from state file
  droplet_id, droplet_name, droplet_ip = read_state_file()
  
  if not droplet_id:
    return False
  
  headers = {
    "Content-Type": "application/json", 
    "Authorization": f"Bearer {api_token}"
  }
  
  print(f"[*] Destroying droplet {droplet_name} with ID: {droplet_id}")
  
  # Delete the droplet using the ID from state file
  delete_url = f"https://api.digitalocean.com/v2/droplets/{droplet_id}"
  response = requests.delete(delete_url, headers=headers)
  
  if response.status_code == 204:
    print(f"[✓] Droplet {droplet_name} (ID: {droplet_id}) has been destroyed")
    # Remove state file after successful destruction
    delete_state_file()
    return True
  else:
    print(f"[!] Error destroying droplet: {response.status_code} - {response.text}")
    return False

def main(argv):
  if len(argv) < 2:
    print("Usage: python terraform_parser.py <terraform_file> [destroy]")
    sys.exit(1)
    
  input_stream = FileStream(argv[1])
  lexer = TerraformSubsetLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = TerraformSubsetParser(stream)
  tree = parser.terraform()

  listener = TerraformApplyListener()
  walker = ParseTreeWalker()
  walker.walk(listener, tree)

  token = listener.resolve_token()
  
  # Check if destroy mode is requested via command line argument or destroy block
  destroy_requested = len(argv) > 2 and argv[2] == "destroy"
  
  if listener.destroy_mode or destroy_requested:
    # Destroy mode
    print("[*] Destroy mode activated")
    destroy_droplet(token)
  else:
    # Apply mode (create)
    if not listener.droplet_config:
      raise Exception("Missing digitalocean_droplet resource.")

    droplet_id, ip = create_droplet(token, listener.droplet_config)
    print(f"[✓] Droplet created with ID: {droplet_id}")
    print(f"[✓] Droplet available at IP: {ip}")

if __name__ == "__main__":
  main(sys.argv)
