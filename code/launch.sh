#!/bin/bash

# Se redirige la mayorías de las salidas estandar para dejar más limpia la consola

echo "Descargando las dependencias necesarias"

# Descargar las dependencias
bash setup.sh 1> /dev/null

echo "Obteniendo la red de interraccion a traves de StringDB"

# Obtener la red de interacción
python3 network_obtention.py 1> /dev/null

echo "Procesando la red con igraph"

# Cargamos la red en R y devolvemos los genes de interes
Rscript network_evaluation.R 1> /dev/null
