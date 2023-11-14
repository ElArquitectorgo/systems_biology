#!/bin/bash

# Crear las carpetas donde estarán las librerias de python y de R
mkdir -p ../software
mkdir -p ../software/deps_Python
mkdir -p ../software/deps_R

# Instalar dependencias desde el archivo requirements_python.txt
pip install -r ../results/requirements_python.txt --target=../software/deps_Python

# Instalar dependencias desde el archivo requirements_R.txt
Rscript -e 'install.packages(readLines("../results/requirements_R.txt"), lib="../software/deps_R")'
# IMPORTANTE EL BUENO ES EL DE ABAJO, DESCOMENTAR PARA ENTREGA FINAL
# Rscript -e 'install.packages(readLines("../results/requirements_R.txt"), dependencies = TRUE, lib="../software/deps_R")'
