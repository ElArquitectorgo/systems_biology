import requests 
import os
import json
import pandas as pd

# Definicion de variables
max_fdr = 0.01 # False Discovery Rate
specie = 9606 # Homo Sapiens
string_api_url = "https://version-11-5.string-db.org/api" # APIRest
output_format = "json" 
method = "enrichment" # haremos un enriquecimiento funcional
get_ids = "get_string_ids" # metodo para obtener los id de stringdb

# Obtener la ruta del directorio actual (donde está el script)
path_script = os.path.dirname(os.path.realpath(__file__))
gene_names = []
file_path = os.path.join(path_script, "../results/interest_nodes.csv")

# Cargar los nombres de los genes en una lista, excluyendo el encabezado
with open(file_path, 'r') as file:
    gene_names = [line.strip() for line in file]

# url para obtener los string ids de los genes de interes
ids_url = "/".join([string_api_url, output_format, get_ids])
string_ids = []
for gene in gene_names: 
    params = {
        "identifier": gene.strip(),
        "species": specie
                }
    # enviamos la peticion
    response = requests.get(ids_url, params=params)
    data = response.json()
    string_ids.append(data[0]['stringId'])

# creamos la url para el enriquecimiento funcional
request_url = "/".join([string_api_url, output_format, method])

# parametros para el enriquecimiento funcional
params = {

    "identifiers" : "%0d".join(string_ids), 
    "species" : specie # identificador de la especie en NCBI
}
# enviamos la peticion
response = requests.post(request_url, data=params)

# cargamos los datos de la respuesta en formato JSON
data = json.loads(response.text)

# guardamos la informacion en un DataFrame
df_rows = []

for row in data:
    term = row["term"]
    preferred_names = ",".join(row["preferredNames"])
    fdr = float(row["fdr"])
    p_value = float(row["p_value"])
    description = row["description"]
    category = row["category"]
    # filtramos por el fdr
    if fdr < max_fdr:
        df_rows.append([term, preferred_names, fdr, category, p_value, description])
# creamos el DataFrame
df = pd.DataFrame(df_rows, columns=["Term", "Preferred Names", "FDR", "Category", "p-value", "Description"])

# construimos la ruta del archivo de salida
output = os.path.join(path_script, "../results/functional_enrichment.csv")

# guardamos el DataFrame en un archivo csv
df.to_csv(output, index=False)
print(string_ids)

