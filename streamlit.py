import json
import streamlit as st
import pandas as pd
from database import IniciarTienda


tienda = IniciarTienda("Tienda")

with open("TiendaRopa.json") as file:
    data = json.load(file)
    tienda.insert_many(data)

    print("Datos cargados correctamente.")

data = list(tienda.find({}, {"_id": 0}))
df = pd.DataFrame(data)

st.title("Tienda")
st.metric("Total de Productos", len(df))
st.dataframe(df)

categorias = df['categoria'].value_counts()
st.bar_chart(categorias)