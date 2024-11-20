import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Configuración del dashboard
st.set_page_config(page_title="Dashboard Interactivo - Histidina", layout="wide")

# Título del dashboard
st.title("Dashboard Interactivo: Histidina")

# Introducción
st.markdown("""
### ¿Qué es la Histidina?
La **histidina** es un aminoácido esencial involucrado en la síntesis de proteínas, el metabolismo celular y el sistema inmunológico.  
Este dashboard te permite explorar datos relacionados con la histidina, sus propiedades químicas y biológicas.
""")

# Sidebar con controles interactivos
st.sidebar.header("Controles Interactivos")
opcion = st.sidebar.radio("Elige una opción para explorar:", ["Propiedades Básicas", "Gráficos Interactivos", "Visualización de Datos"])

# --- SECCIÓN 1: Propiedades Básicas ---
if opcion == "Propiedades Básicas":
    st.header("Propiedades Básicas de la Histidina")
    
    # Tabla con información básica
    propiedades = {
        "Propiedad": ["Fórmula Química", "Masa Molecular (g/mol)", "pKa", "Punto Isoeléctrico (pI)", "Clasificación"],
        "Valor": ["C6H9N3O2", "155.15", "6.0", "7.6", "Aminoácido esencial"],
    }
    df_propiedades = pd.DataFrame(propiedades)
    st.table(df_propiedades)
    
    # Imagen de estructura química (opcional)
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/0a/Histidine.png", caption="Estructura química de la Histidina", use_column_width=True)

# --- SECCIÓN 2: Gráficos Interactivos ---
elif opcion == "Gráficos Interactivos":
    st.header("Gráficos Interactivos")
    
    # Datos de ejemplo para análisis
    data = pd.DataFrame({
        "pH": [3, 4, 5, 6, 7, 8, 9],
        "Solubilidad (mg/mL)": [30, 50, 65, 75, 70, 55, 40],
        "Absorción UV (nm)": [220, 225, 230, 235, 240, 245, 250],
    })
    
    # Gráfico interactivo con Plotly
    fig = px.line(data, x="pH", y="Solubilidad (mg/mL)", markers=True, title="Solubilidad de la Histidina según el pH")
    st.plotly_chart(fig)
    
    # Slider interactivo para rango de pH
    rango_pH = st.slider("Selecciona el rango de pH:", min_value=3, max_value=9, value=(4, 8))
    filtro_data = data[(data["pH"] >= rango_pH[0]) & (data["pH"] <= rango_pH[1])]
    st.write(f"Datos filtrados entre pH {rango_pH[0]} y {rango_pH[1]}:")
    st.dataframe(filtro_data)

# --- SECCIÓN 3: Visualización de Datos ---
elif opcion == "Visualización de Datos":
    st.header("Visualización de Datos Relacionados con la Histidina")
    
    # Datos adicionales (ejemplo)
    bio_data = pd.DataFrame({
        "Tejido": ["Músculo", "Cerebro", "Hígado", "Riñón", "Plasma"],
        "Concentración (μM)": [20, 15, 25, 30, 10],
    })
    
    # Gráfico de barras interactivo
    fig_barras = px.bar(bio_data, x="Tejido", y="Concentración (μM)", color="Tejido", title="Concentración de Histidina en Diferentes Tejidos")
    st.plotly_chart(fig_barras)
    
    # Información adicional
    st.markdown("""
    **Nota:** La histidina juega un papel crucial en la regulación del pH en los tejidos y la síntesis de histamina.
    """)
