#!/bin/bash

# Crear las carpetas donde estarán las librerias de python y de R
mkdir -p ../software
mkdir -p ../software/deps_Python
mkdir -p ../software/deps_R

# Limiamos la cache de pip para evitarnos problemas
python3 -m pip cache purge

# Instalar dependencias desde el archivo requirements_python.txt
python3 -m pip install -r ../results/requirements_python.txt --target=../software/deps_Python 1> /dev/null

# Instalar dependencias desde el archivo requirements_R.txt
Rscript -e 'install.packages(readLines("../results/requirements_R.txt"), repos="http://cran.us.r-project.org", dependencies=TRUE, lib="../software/deps_R")' 1> /dev/null
