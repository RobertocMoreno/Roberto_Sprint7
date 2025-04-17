import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Crea un gráfico de los vehículos')        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón para histograma
disp_button = st.button('Contruir una gráfico de dispersión') # crear un botón para gráfico de dispersión
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y='price')
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)