# Uso de la Biología de Sistemas en el estudio de la diabetes materna

sistems_biology es un proyecto de la asignatura Biología de Sistemas en Ingeniería de la Salud. Este trabajo aborda el estudio de la relación entre el gen GNB3 y la diabetes materna usando técnicas de biología de sistemas y análisis de redes.

## Participantes

- Víctor Guirado Osorio
- Susana Rocío Fernández Giaccomassi
- Pablo Bermúdez Gámez
- Juan Carlos Vergara Ruz

## Requisitos del sistema

- Sitema operativo: Linux y macOS
- Python 3.x
- Librerías Python adicionales: `openpyxl`, `Stringdb`, `Pandas`, `iGraph`, `Cairocffi` (se instalarán automáticamente en un entorno virtual)

## Instalación y configuración
1. Clona el repositorio en tu máquina local.
2. Asegúrate de que Python 3.x está instalado en tu sistema, con el módulo `venv`.

```
git clone https://github.com/ElArquitectorgo/systems_biology.git
python3 -m pip install virtualenv
```

> [!WARNING]
> En macOS, es posible que se muestre un mensaje solicitando la instalación de `cairocffi` o `pycairo`. Aunque `cairocffi` ya está incluido en el `requirements.txt` y se instalará en el entorno virtual, puede ser necesario instalar `pycairo` en el entorno virtual para un correcto funcionamiento. Para ello, añade la línea `pycairo==1.25.1` al `requirements.txt` antes de ejecutar `launch.sh` o instala directamente el paquete en tu máquina con `pip install pycairo==1.25.1`.

## Uso
Para ejecutar los scripts:
Ejecute `launch.sh` para iniciar el análisis:
```
cd code
./launch.sh
```
Los scripts se ejecutarán en el orden necesario, realizando el análisis de red y el enriquecimiento funcional. Una vez que la ejecución termine, puedes ver los resultados en el directorio `results`


## Contenido
- `network_obtention.py`: Extrae genes relacionados con la diabetes materna y construye la red de genes.
- `network_evaluation.py`: Evalúa la red e identifica comunidades de genes.
- `functional_enrichment.py`: Realiza un análisis de enriquecimiento funcional de genes dentro de la comunidad GNB3, amplía la red y hace un segundo análisis de enriquecimiento funcional.
- `launch.sh`: Script Shell que crea un entorno virtual usando el módulo `venv` de Python, instala las dependencias necesarias e inicia los scripts Python en la secuencia correcta.
- `setup.sh`: Configura el entorno, incluyendo la instalación de las librerías Python necesarias.
- `requirements.txt`: Lista todas las dependencias de Python para el proyecto.
- `report.pdf`: Informe de investigación detallado que describe la metodología, los resultados y su discusión.
