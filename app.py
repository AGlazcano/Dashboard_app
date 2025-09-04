import streamlit as st
st.header(' Comparativa de trabajos ')
st.write('Grafico , relacion entre   trabajos* sexo')



from pathlib import Path
import pandas as pd

# Definir ruta base y archivo
base_dir = Path.cwd()
csv_path = base_dir / 'data' / 'people-100.csv'
df = pd.read_csv(
        csv_path,
        sep=',',             # separador por defecto
        encoding='utf-8',    # ajustable según origen del archivo
        header=0  ,           # primera fila como cabecera
        index_col=0        # opcional: usar primera columna como índice
    )

df.head()