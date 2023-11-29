from igraph import Graph, plot
import pandas as pd
import os

# Obtener la ruta absoluta del script actual
path_script = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo CSV
csv_path = os.path.join(path_script, '..', 'results', 'network.csv')

# Cargar datos desde el archivo CSV
data = pd.read_csv(csv_path)

g = Graph.TupleList(data.itertuples(index=False),directed=False)
g = g.simplify()

colors = ["lightgreen" if name == "GNB3" else "#FF6961" for name in g.vs["name"]]

# Guardar el grafo en formato SVG
plot(g, os.path.join(path_script, '..', 'results', 'network.svg'), vertex_label=g.vs["name"], vertex_label_size=10, vertex_label_color="black",
     vertex_size=12, vertex_label_dist=2, edge_color="darkgray", vertex_color=colors)

# Calcular las comunidades mediante el método "cluster_edge_betweenness"
ceb = g.community_edge_betweenness()
cl = ceb.as_clustering()

# Guardar el grafo de comunidades en formato SVG
plot(cl, os.path.join(path_script, '..', 'results', 'comunidades.svg'), mark_groups=True, vertex_label=g.vs["name"], vertex_label_size=10, vertex_label_color="black",
     vertex_size=12, vertex_label_dist=2, edge_color="darkgray", vertex_color="#FF6961")

# Obtener los nodos en la misma comunidad que nuestro nodo de interés
for comunidad in (cl):
    nombres = g.vs[comunidad]["name"]
    if "GNB3" in nombres:
        # Guardar los nombres de los nodos en un archivo CSV
        nombres_df = pd.DataFrame({'Nombres': nombres})
        csv_path = os.path.join(path_script, '..', 'results', 'interest_nodes.csv')
        nombres_df.to_csv(csv_path, index=False, header=False)
        break
