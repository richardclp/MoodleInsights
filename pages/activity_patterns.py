import streamlit as st
import altair as alt
import pandas as pd

def show(data):
    st.header("Patrones de Actividad")
    
    # Convertir la columna de hora a formato datetime
    data['Hora de Conexión'] = pd.to_datetime(data['Hora de Conexión'], format='%H:%M').dt.hour
    activity_by_hour = data.groupby('Hora de Conexión').size().reset_index(name='Número de Conexiones')
    
    # Crear gráfico de líneas
    st.write("Actividad de Estudiantes por Hora")
    line_chart = alt.Chart(activity_by_hour).mark_line().encode(
        x='Hora de Conexión',
        y='Número de Conexiones'
    ).properties(width=700)
    st.altair_chart(line_chart, use_container_width=True)
