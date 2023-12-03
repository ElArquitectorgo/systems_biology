#!/bin/bash

echo "Creando el entorno virtual"
python3 -m venv .venv
source .venv/bin/activate

echo "Instalando las dependencias"

bash setup.sh 1> /dev/null

echo "Obtención de la red"
python network_obtention.py

echo "Evaluación de la red"
python network_evaluation.py network.csv network.svg comunidades.svg interest_nodes.csv

echo "Enriquecimiento funcional"
python functional_enrichment.py interest_nodes.csv enrichment.csv enrichment_expandido.csv

deactivate

# Copiar resultados para el reporte
cd ..
cp results/comunidades.svg results/network.svg report/figures/
