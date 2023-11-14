#!/bin/bash

# Descargar las dependencias
bash setup.sh

# Obtener la red de interacción
python3 network_obtention.py

# Cargamos la red en R y devolvemos los genes de interes
Rscript network_evaluation.R
