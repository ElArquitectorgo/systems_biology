import os
import sys
import csv
import pandas as pd
import stringdb

"""
Calcular el enriquecimiento funcional de un conjunto de genes. 
Adicionalmente se expande ese conjunto con 16 nodos más y se 
calcula nuevamente el enriquecimiento.
"""

# Obtener la ruta del directorio actual (donde está el script)
path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(path, '..', 'results', sys.argv[1])

# Extraer genes desde csv
genes = []
with open(csv_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        genes.append(''.join(row))

# Crear red ampliada
new_network = stringdb.get_network(identifiers=genes, species = 9606, add_nodes=16)

# Obtener los valores únicos
ids = pd.concat([new_network['stringId_A'], new_network['stringId_B']])
unique_ids = ids.unique()

# Definir funcion para enrriquecimiento
def get_functional_enrichment(genes):
    enrichment_df = stringdb.get_enrichment(identifiers=genes, species = 9606)

    filtered_df = enrichment_df[enrichment_df['preferredNames'].str.contains('GNB3')]
    result = filtered_df[['preferredNames', 'description', 'p_value', 'fdr', 'category', 'term']]
    return result

first_result = get_functional_enrichment(genes)
second_result = get_functional_enrichment(unique_ids)

# Construimos la ruta del archivo de salida
first_output = os.path.join(path, f"../results/{sys.argv[2]}")
second_output = os.path.join(path, f"../results/{sys.argv[3]}")
# Guardamos el DataFrame en un archivo csv
first_result.to_csv(first_output, index=False)
second_result.to_csv(second_output, index=False)
