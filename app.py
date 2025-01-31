import streamlit as st
from transformers import pipeline

# Título de la aplicación
st.title('Formulario de Viabilidad de Negocio')

# Ingreso de datos del negocio
nombre_negocio = st.text_input('Nombre del Negocio')
descripcion_producto = st.text_area('Descripción del Producto/Servicio')
sector = st.selectbox('Selecciona el Sector', ['Tecnología', 'Salud', 'Educación', 'Retail'])
presupuesto_inicial = st.number_input('Presupuesto Inicial ($)', min_value=0)

# Botón para procesar el formulario
if st.button('Analizar'):
    # Mostrar los datos ingresados
    st.write('Nombre del Negocio:', nombre_negocio)
    st.write('Descripción:', descripcion_producto)
    st.write('Sector:', sector)
    st.write('Presupuesto Inicial:', presupuesto_inicial)

    # Análisis de sentimiento utilizando Hugging Face
    model = pipeline('sentiment-analysis')
    resultado_sentimiento = model(descripcion_producto)

    # Mostrar el análisis de sentimiento
    if resultado_sentimiento[0]['label'] == 'POSITIVE':
        st.write('El análisis de sentimiento es positivo sobre el producto.')
    else:
        st.write('El análisis de sentimiento es negativo sobre el producto.')

    # Realizamos un análisis simple del presupuesto
    if presupuesto_inicial >= 1000:
        st.write('¡El presupuesto es suficiente para empezar en este sector!')
    else:
        st.write('El presupuesto podría ser limitado para competir en este sector. Considera aumentar el presupuesto o comenzar con un enfoque más pequeño.')
    
    st.write("¡Recuerda siempre validar la viabilidad de tu idea en el mercado y ajustarla según el feedback!")
