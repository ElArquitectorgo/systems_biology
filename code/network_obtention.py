import os
import pandas as pd
import stringdb

"""
Obtiene la red de interacciónes de los genes dados.
"""

# Obtener la ruta del directorio actual (donde está el script)
path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta del archivo Excel usando una ruta relativa
path_excel = os.path.join(path, '..', 'results', 'genes_for_HP_0009800.xlsx')

# Cargar el archivo XLSX en un DataFrame de pandas
genes = pd.read_excel(path_excel)

# Nos quedamos con los identificadores de los genes
genes_ids = genes['GENE_ENTREZ_ID']
genes_ids = list(map(str, genes_ids))
genes_ids.append("2784")

network = stringdb.get_network(identifiers=genes_ids, species=9606)
n = pd.DataFrame()
n = network[['preferredName_A', 'preferredName_B']]
n.to_csv(os.path.join(path, '..', 'results', 'network.csv'), header=None, index=None, sep=',', mode='w')