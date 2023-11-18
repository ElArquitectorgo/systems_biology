#!/bin/bash

# Crear las carpetas donde estarán las librerias de python y de R
mkdir -p ../software
mkdir -p ../software/deps

# Limiamos la cache de pip para evitarnos problemas
python3 -m pip cache purge

# Instalar dependencias desde el archivo requirements_python.txt
python3 -m pip install -r ../results/requirements.txt --target=../software/deps 1> /dev/null
