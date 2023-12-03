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
python functional_enrichment.py interest_nodes.csv network_expandido.csv enrichment.csv enrichment_expandido.csv

echo "Evaluación de la red expandida"
python network_evaluation.py network_expandido.csv network_expandido.svg comunidades_expandido.svg nodes_expandido.csv

deactivate

# Copiar resultados para el reporte
cd ..
cp results/comunidades.svg results/comunidades_expandido.svg results/network.svg results/network_expandido.svg report/figures/
