import os
import sys
import json

# Agregar al sys.path la ruta de la carpeta deps_Python
sys.path.append(os.path.join(os.path.dirname(__file__), "../software/deps_Python"))

import pandas as pd
import requests

# Obtener la ruta del directorio actual (donde está el script)
path_script = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta del archivo Excel usando una ruta relativa
path_excel = os.path.join(path_script, '..', 'results', 'genes_for_HP_0009800.xlsx')

# Cargar el archivo XLSX en un DataFrame de pandas
genes = pd.read_excel(path_excel)

# Nos quedamos con los identificadores de los genes
genes_ids = genes['GENE_ENTREZ_ID']

# Declaramos la APIRest que vamos a utilizar
string_api_url = "https://version-11-5.string-db.org/api"

# Anyadimos el gen de interes
genes_ids = list(map(str, genes_ids))
genes_ids.append("2784")

params = {
    "identifiers" : "%0d".join(genes_ids), # your genes
    "species" : 9606 # species NCBI identifier 
}

# Construimos la direccion url completa
request_url = "/".join([string_api_url, "json", "network"])

# Mandamos la petición y la recogemos
response = requests.post(request_url, data=params)

# Cargamos los datos de la respuesta en formato JSON
data = json.loads(response.text)

# Los guardamos en un Dataframe
network = pd.DataFrame(data)

# Nos quedamos con la información relevante
network = network[['preferredName_A', 'preferredName_B']]

# Guardamos la red en formato csv
path_output = os.path.join(path_script, '..', 'results', 'network.csv')
network.to_csv(path_output, index=False)

