import os
import pandas as pd
import stringdb
from igraph import Graph

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

# Obtener la red de interacciónes de los genes dados
network_without_gnb3 = stringdb.get_network(identifiers=genes_ids, species=9606)
edges = [(row['preferredName_A'], row['preferredName_B']) for index, row in network_without_gnb3.iterrows()]
G = Graph.TupleList(edges, directed=False)

# Almacenar la cantidad de nodos y aristas de la red original
nodes_edges_count = pd.DataFrame({'Nodes': [len(G.vs)], 'Edges': [len(G.es)]})
nodes_edges_count.to_csv(os.path.join(path, '..', 'results', 'nodes_edges_count_before_gnb3.csv'), index=False)


genes_ids.append("2784")

network = stringdb.get_network(identifiers=genes_ids, species=9606)
n = pd.DataFrame()
n = network[['preferredName_A', 'preferredName_B']]
n.to_csv(os.path.join(path, '..', 'results', 'network.csv'), header=None, index=None, sep=',', mode='w')