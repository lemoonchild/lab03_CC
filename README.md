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