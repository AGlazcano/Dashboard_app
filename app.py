import streamlit as st
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Cargar CSV
base_dir = Path.cwd()
csv_path = base_dir / 'data' / 'people-100.csv'

try:
    df = pd.read_csv(csv_path, sep=',', encoding='utf-8', header=0, index_col=0)
    st.success("✅ Archivo cargado correctamente.")
    
    # Estandarización de nombres de columnas
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
    
except Exception as e:
    st.error(f"❌ Error al cargar el archivo: {e}")
    st.stop()
    
    
#----------------------------------------    
# Título
st.title("📊 Dashboard_app")
#----------------------------------------
# Botones interactivos
if st.button("Mostrar tabla completa"):
    st.subheader("Vista previa del DataFrame")
    st.dataframe(df)

#---------------------------------------------------------------------------------------------
if st.button("📊 Mostrar gráfico de profesiones por sexo"):
    # Agrupar datos
    grupo = df.groupby(['job_title', 'sex']).size().reset_index(name='count')

    # Crear figura y graficar
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=grupo, x='job_title', y='count', hue='sex', ax=ax)
    plt.xticks(rotation=45, ha='right')
    plt.title('Distribución de profesiones por sexo')
    plt.tight_layout()

    # Mostrar gráfico en Streamlit
    st.subheader("📊 Distribución de profesiones por sexo")
    st.pyplot(fig)
#---------------------------------------------------------------------------------------------
    
    # Agrupar por job_title y contar ocurrencias
grupo = df['job_title'].value_counts().reset_index()
grupo.columns = ['job_title', 'count']

# Botón para mostrar gráfico
if st.button("📊 Mostrar frecuencia de profesiones"):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=grupo, x='job_title', y='count', palette='Set2')
    plt.xticks(rotation=45, ha='right')
    plt.title('Frecuencia de profesiones')
    plt.tight_layout()
    st.pyplot(fig)
#---------------------------------------------------------
grupo = df['job_title'].value_counts().reset_index()
grupo.columns = ['job_title', 'count']

# Botón para mostrar gráfico
if st.button("📌 Mostrar gráfico de dispersión por profesión"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(grupo['job_title'], grupo['count'], color='teal', s=100, alpha=0.7)
    ax.set_title("Dispersión de frecuencia por profesión")
    ax.set_xlabel("Profesión")
    ax.set_ylabel("Frecuencia")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)
