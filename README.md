# lab03_CC
Laboratorio 03: Uso de ANTLR para Parsear Terraform y Administrar Droplets de DigitalOcean

## Ejecución Docker - ANTLR

### Directorio de ejecución

```bash
cd lab-3/antlr
```

### Ejecución de Docker

```bash
docker build -t antlr-lab . && docker run -it -v "$(pwd)/program:/program" antlr-lab bash
```

### Crear llave SSH 
```bash
ssh-keygen -t ed25519 -f /root/.ssh/do-droplet-key -N ""
ls -l /root/.ssh/do-droplet-key*
```

#### Agregar la llave SSH a DigitalOcean
- Ir a la pestaña de API y generar un API Key con los scopes de: 

| Recurso      | Operaciones          |
| ------------ | -------------------- |
| **ssh\_key** | read, create         |
| **droplet**  | create, read, delete |
| **account**  | read                 |

- Colocar esa API Key en `main.tf`.

- Hacer `cat` de la llave ssh.pub y copiarla:
```bash
cat /root/.ssh/do-droplet-key.pub
```

- En DigitalOcean, ir a `Settings`, `Security` y agregar la llave ssh.pub.

### Levantar ANTLR

```bash
antlr -Dlanguage=Python3 TerraformSubset.g4
```
### Ejecución de parser como Driver

#### Apply
```bash
python3 terraform_parser.py <terraform_file>
```

#### Destroy
```bash
python3 terraform_parser.py <terraform_file> destroy
```

Nota: En `evidence.txt` creado se podrá ver la conexión exitosa, luego del comando `apply`.