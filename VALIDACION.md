# Validación local · Sprint 7

Fecha: 8 de noviembre de 2026, zona America/Mexico_City.

## Alcance

Se desarrolló el proyecto indicado en la
[lección de TripleTen](https://tripleten.com/trainer/data-scientist/lesson/c779060b-b834-47b3-ac73-7fc21b61558b/?tab=0).
Las comprobaciones siguientes corresponden al entorno local de esa fecha.
La publicación en GitHub se registra al final; la revisión del autor, el
despliegue en Render y la aceptación del revisor siguen pendientes.

## Entorno comprobado

- Python 3.11.9, entorno virtual `vehicles_env`.
- pandas 3.1.1, Plotly 7.1.0 y Streamlit 1.67.0.
- `requirements.txt` mantiene las tres dependencias sin versiones, como pide
  la lección. Las versiones anteriores describen únicamente esta validación.
- `python -m pip check`: sin dependencias incompatibles.

## Dataset

- Archivo original: `vehicles_us.csv`, descargado del enlace de la lección.
- 51,525 filas, 13 columnas, 0 filas completamente duplicadas.
- 7,892 valores ausentes en `odometer`; 0 en `price`.
- 43,633 anuncios en cada gráfico, sin imputación ni eliminación de extremos.
- SHA-256: `f26e6a2e3d365156d09cec544936a975654f8249c58327fc5360f3826846f290`.

## Comprobaciones realizadas

1. **Pruebas automatizadas:** `python -m unittest discover -s tests -v`.
   Tres pruebas aprobadas: carga y contenido exacto de los gráficos, cuatro
   combinaciones de las casillas y mensaje al no poder leer el CSV. También se
   ejecutaron desde fuera de la carpeta del proyecto para comprobar las rutas.
2. **Notebook:** ejecución completa mediante `nbclient`, con el directorio de
   trabajo en `notebooks`. Cinco celdas de código ejecutadas, dos salidas Plotly,
   sin salidas de error; estructura validada con `nbformat`. Los resultados
   están guardados en `notebooks/EDA.ipynb`.
3. **Servidor local:** Streamlit iniciado en `127.0.0.1:8501`;
   `GET /_stcore/health` respondió `ok` con HTTP 200.
4. **Chrome:** encabezado, histograma y dispersión renderizados; se comprobó
   que desmarcar la casilla del histograma lo oculta y que volver a marcarla lo
   restaura. Las cuatro combinaciones se cubren en la prueba automatizada.
5. **Evidencia visual local:** `.work/preview-histogram.jpg` y
   `.work/preview-scatter.jpg`, excluidas del repositorio por `.gitignore`.

## Pendientes para entregar

- Revisión y correcciones del autor.
- Crear/configurar el servicio de Render, desplegar y probar la URL pública.
- Sustituir el texto pendiente del README por el enlace real de Render.
- Enviar el enlace de GitHub al revisor de TripleTen.

El README contiene los comandos de instalación, ejecución y publicación. Esta
validación local no acredita el despliegue ni la aceptación del proyecto.

## Publicación en GitHub · 11 de noviembre de 2026

Repositorio público:
[Edward-TL/eda-vehiculos-tripleten](https://github.com/Edward-TL/eda-vehiculos-tripleten),
rama `main`, conectado como remoto `origin` del proyecto local.

Se publica el código validado el 8 de noviembre, junto con la documentación
actualizada para indicar el repositorio. El entorno virtual, los archivos
temporales y las capturas locales se mantienen excluidos. Las pruebas
documentadas arriba corresponden al 8 de noviembre; esta publicación no
modifica el código de la aplicación ni el notebook.
