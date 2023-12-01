#!/bin/bash

echo "Creando el entorno virtual"
python3 -m venv .venv
source .venv/bin/activate

echo "Instalando las dependencias"

bash setup.sh 1> /dev/null

echo "Obtención de la red"
python network_obtention.py

echo "Evaluación de la red"
python network_evaluation.py _

echo "Enriquecimiento funcional"
python functional_enrichment.py interest_nodes.csv first_functional_enrichment.csv second_functional_enrichment.csv

deactivate
