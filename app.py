from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Anuncios de vehículos", layout="wide")
st.header("Análisis de anuncios de venta de vehículos")
st.write(
    "Explora la distribución del odómetro y su relación con el precio anunciado. "
    "Selecciona las casillas para mostrar u ocultar cada gráfico."
)


@st.cache_data
def load_data():
    return pd.read_csv(Path(__file__).resolve().parent / "vehicles_us.csv")


try:
    car_data = load_data()
except (OSError, pd.errors.ParserError):
    st.error("No se pudo leer vehicles_us.csv. Comprueba el archivo del proyecto.")
    st.stop()

st.caption(f"Conjunto de datos: {len(car_data):,} anuncios de vehículos.")

with st.expander("Ver una muestra de los datos originales"):
    st.dataframe(car_data.head(100), hide_index=True)

if st.checkbox("Mostrar histograma del odómetro", value=True):
    st.subheader("Distribución del odómetro")
    histogram_data = car_data.dropna(subset=["odometer"])
    st.write(
        f"Se incluyen {len(histogram_data):,} anuncios con odómetro registrado. "
        f"Se omiten {car_data['odometer'].isna().sum():,} registros sin este dato."
    )
    histogram = px.histogram(
        histogram_data,
        x="odometer",
        nbins=50,
        labels={"odometer": "Lectura del odómetro"},
        title="Frecuencia de las lecturas del odómetro",
    )
    histogram.update_layout(yaxis_title="Cantidad de anuncios", bargap=0.05)
    st.plotly_chart(histogram, width="stretch", key="histogram")

if st.checkbox("Mostrar dispersión entre odómetro y precio", value=True):
    st.subheader("Relación entre odómetro y precio")
    scatter_data = car_data.dropna(subset=["odometer", "price"])
    st.write(
        f"Cada punto representa uno de los {len(scatter_data):,} anuncios "
        "con odómetro y precio registrados."
    )
    scatter = px.scatter(
        scatter_data,
        x="odometer",
        y="price",
        opacity=0.35,
        labels={"odometer": "Lectura del odómetro", "price": "Precio anunciado"},
        title="Precio anunciado según la lectura del odómetro",
    )
    st.plotly_chart(scatter, width="stretch", key="scatter")

st.caption(
    "Los datos originales se conservan: no se rellenan valores ausentes ni se "
    "eliminan valores extremos. Cada gráfico omite "
    "únicamente las filas sin datos en sus variables."
)
