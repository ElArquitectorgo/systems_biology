import os
import sys
import subprocess
import csv
import pandas as pd
import stringdb

# Obtener la ruta del directorio actual (donde está el script)
path_script = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(path_script, '..', 'results', sys.argv[1])

# Extraer genes desde csv
genes = []
with open(csv_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        genes.append(''.join(row))

# Crear red ampliada
new_network = stringdb.get_network(identifiers=genes, species = 9606, add_nodes=16)

n = pd.DataFrame()
n = new_network[['preferredName_A', 'preferredName_B']]

# Importar red original y expandir con la nueva
original_network = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'results', 'network.csv'))
original_network.columns = ['preferredName_A', 'preferredName_B']

expanded_network = pd.merge(n, original_network, how='outer')
expanded_network.to_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'results', 'network.csv'), header=None, index=None, sep=',', mode='w')

# Ejecutar 'network_evaluation.py' para la nueva red
subprocess.run(["python", "network_evaluation.py", '_expandida'])

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
first_output = os.path.join(path_script, f"../results/{sys.argv[2]}")
second_output = os.path.join(path_script, f"../results/{sys.argv[3]}")
# Guardamos el DataFrame en un archivo csv
first_result.to_csv(first_output, index=False)
second_result.to_csv(second_output, index=False)
