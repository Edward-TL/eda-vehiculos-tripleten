# Anuncios de vehículos · Sprint 7

Aplicación de Streamlit para explorar el conjunto de datos de anuncios de venta
de vehículos proporcionado por TripleTen. Incluye un histograma del odómetro y
un gráfico de dispersión del precio frente al odómetro, construidos con Plotly.
Dos casillas permiten mostrar u ocultar los gráficos de forma independiente.
También se puede consultar una muestra de los datos originales.

**Repositorio público:** [Edward-TL/eda-vehiculos-tripleten](https://github.com/Edward-TL/eda-vehiculos-tripleten).

**Aplicación en Render:** pendiente de publicación por el autor. Después del
despliegue, sustituye esta línea por el enlace real a la aplicación.

## Archivos

```text
app.py                   Aplicación web
vehicles_us.csv          Dataset original de la lección
notebooks/EDA.ipynb       Análisis exploratorio con resultados y gráficos
requirements.txt         Dependencias de la aplicación, sin versiones
requirements-dev.txt     Dependencias adicionales para ejecutar el notebook
tests/test_app.py        Pruebas de la aplicación con Streamlit AppTest
.gitignore               Exclusiones de Python, Jupyter y archivos locales
.streamlit/config.toml   Desactiva el envío de estadísticas de uso
.vscode/settings.json    Selecciona el entorno virtual local
VALIDACION.md            Evidencia de la validación local
```

## Ejecutar localmente

Abre esta carpeta como proyecto en VS Code. Se utilizó Python 3.11.9 para la
validación. Desde la raíz del proyecto, crea y activa un entorno virtual:

```bash
python3 -m venv vehicles_env
source vehicles_env/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

En Windows, activa el entorno con `vehicles_env\Scripts\activate`.
Abre la dirección que indique Streamlit, normalmente
[http://localhost:8501](http://localhost:8501). Para detenerlo, pulsa `Ctrl+C`
en la terminal. El CSV se busca junto a `app.py`, independientemente del
directorio desde el que se inicie la aplicación.

## Notebook

Con el mismo entorno activado:

```bash
python -m pip install -r requirements-dev.txt
```

Abre `notebooks/EDA.ipynb` en VS Code, selecciona el intérprete de `vehicles_env`
y ejecuta todas las celdas. Puede iniciarse desde la raíz del proyecto o desde
`notebooks`.

El dataset tiene 51,525 anuncios y 13 columnas. Los dos gráficos incluyen los
43,633 anuncios con odómetro registrado; no hay precios ausentes. El CSV no se
modifica ni se imputan valores. Se conservan los valores extremos y cada
visualización omite únicamente las filas que no tienen las variables necesarias.
Los precios son los anunciados: no representan ventas confirmadas.

Fuente: [CSV oficial de TripleTen](https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv).

## Pruebas

Con las dependencias de `requirements.txt` instaladas:

```bash
python -m unittest discover -s tests -v
```

Las pruebas comprueban la carga de la app, los tipos y datos de los gráficos,
las cuatro combinaciones de las casillas y el mensaje cuando no se puede leer
el CSV.

## Actualizar el repositorio y publicar en Render

El proyecto está publicado en el repositorio público
[eda-vehiculos-tripleten](https://github.com/Edward-TL/eda-vehiculos-tripleten),
con la rama `main`. El remoto `origin` del proyecto local apunta a ese
repositorio. El entorno `vehicles_env` queda excluido del repositorio.
Tras revisar y confirmar tus correcciones, súbelas con `git push origin main`.

En Render, crea un **Web Service** conectado a ese repositorio y configura:

| Campo | Valor |
| --- | --- |
| Runtime | Python 3 |
| Build Command | `pip install --upgrade pip && pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT --server.headless true` |
| Health Check Path | `/_stcore/health` |

Si subes el contenido de esta carpeta como raíz del repositorio, deja
**Root Directory** vacío. Si lo incluyes dentro de otro repositorio, indica la
ruta relativa de esta carpeta en ese campo. Usa Python 3.11.9 para reproducir el
entorno validado, mediante la variable `PYTHON_VERSION` de Render.

El comando de inicio escucha en `0.0.0.0` y en el puerto `PORT` que proporciona
Render, según su [documentación de servicios web](https://render.com/docs/web-services#port-binding).

Antes de entregar el proyecto:

1. Revisa y sube tus cambios al repositorio de GitHub.
2. Despliega la aplicación en Render y prueba las dos casillas en la URL pública.
3. Añade el enlace real de Render al principio de este README y súbelo a GitHub.
4. Envía el enlace del repositorio público al revisor de TripleTen.

La cuenta de Render, la publicación y el envío al revisor quedan pendientes de
realizarlos por el autor.
