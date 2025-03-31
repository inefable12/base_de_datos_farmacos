import streamlit as st
import pyodbc
import pandas as pd

# Conectar a la base de datos Access
access_db_path = "DB_FARMACOS.accdb"
conn_str = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + access_db_path
conn = pyodbc.connect(conn_str)

# Obtener nombres de tablas
cursor = conn.cursor()
tables = [row.table_name for row in cursor.tables(tableType="TABLE")]

# Interfaz en Streamlit
st.title("Explorador de Base de Datos Access")
tabla_seleccionada = st.selectbox("Selecciona una tabla:", tables)

# Cargar datos de la tabla seleccionada
df = pd.read_sql(f"SELECT * FROM {tabla_seleccionada}", conn)

# Mostrar tabla en Streamlit
st.write(f"Mostrando datos de {tabla_seleccionada}:")
st.dataframe(df)

# Cerrar conexión
conn.close()
