library(igraph, lib.loc = "../software/deps_R")
#library(igraph)

data <- read.csv("../results/network.csv")

my_network <- graph.data.frame(data, directed = FALSE)

jpeg("../report/figures/network_igraph.jpeg")
# Define un vector de colores para los nodos
# Inicialmente todos los nodos son de color "yellow"
colores_nodos <- rep("yellow", vcount(my_network))  
# Cambia el color del nodo con el nombre "GNB3" a rojo
colores_nodos[V(my_network)$name == "GNB3"] <- "red"  
plot(my_network,
     vertex.label.cex = 0.5,
     vertex.label.color = "black",
     vertex.size = 12,
     vertex.color = colores_nodos,
     layout = layout_nicely)
dev.off()

# Calcumos las comunidades mediante el método "cluster_edge_betweenness"
ceb <- cluster_edge_betweenness(my_network)

jpeg("../report/figures/network_comunidades.jpeg")
plot(ceb, my_network,
     vertex.label.cex = 0.5,
     vertex.label.color = "black",
     vertex.size = 12,
     layout = layout_nicely)
dev.off()

# Asignamos a cada nodo su comunidad
comunidades <- membership(ceb)

# Nos quedamos con los nodos que están en la misma comunidad
# que nuestro en de interés
comunidad_interes <- which(comunidades == 2)

# Nos quedamos con los nombres de los nodos
nombres_interes <- V(my_network)$name[comunidad_interes]

# Guarda los nombres de los nodos en un archivo CSV
write.csv(data.frame(nombres_interes),
          file = "../results/interest_nodes.csv",
          row.names = FALSE, quote = FALSE)
