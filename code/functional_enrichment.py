import os
import csv
import pandas as pd
import stringdb

path_script = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(path_script, '..', 'results', 'interest_nodes.csv')

genes = []
with open(csv_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        genes.append(''.join(row))

new_network = stringdb.get_network(identifiers=genes, species = 9606, add_nodes=16)

ids = pd.concat([new_network['stringId_A'], new_network['stringId_B']])
# Obtener los valores únicos
unique_ids = ids.unique()
enrichment_df = stringdb.get_enrichment(identifiers=unique_ids, species = 9606)

filtered_df = enrichment_df[enrichment_df['preferredNames'].str.contains('GNB3')]
result = filtered_df[['preferredNames', 'description', 'p_value', 'fdr', 'category', 'term']]

# construimos la ruta del archivo de salida
output = os.path.join(path_script, "../results/functional_enrichment.csv")

# guardamos el DataFrame en un archivo csv
result.to_csv(output, index=False)

