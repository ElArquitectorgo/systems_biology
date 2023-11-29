import os
import sys
import csv
import pandas as pd
import stringdb

path_script = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(path_script, '..', 'results', sys.argv[1])

genes = []
with open(csv_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        genes.append(''.join(row))

new_network = stringdb.get_network(identifiers=genes, species = 9606, add_nodes=16)

ids = pd.concat([new_network['stringId_A'], new_network['stringId_B']])
# Obtener los valores únicos
unique_ids = ids.unique()

def get_functional_enrichment(genes):
    enrichment_df = stringdb.get_enrichment(identifiers=genes, species = 9606)

    filtered_df = enrichment_df[enrichment_df['preferredNames'].str.contains('GNB3')]
    result = filtered_df[['preferredNames', 'description', 'p_value', 'fdr', 'category', 'term']]
    return result

first_result = get_functional_enrichment(genes)
second_result = get_functional_enrichment(unique_ids)
# construimos la ruta del archivo de salida
first_output = os.path.join(path_script, f"../results/{sys.argv[2]}")
second_output = os.path.join(path_script, f"../results/{sys.argv[3]}")
# guardamos el DataFrame en un archivo csv
first_result.to_csv(first_output, index=False)
second_result.to_csv(second_output, index=False)