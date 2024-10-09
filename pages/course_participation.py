import streamlit as st
import altair as alt
import pandas as pd

def show(data):
    st.header("Participación por Curso")
    
    # Agrupar por curso y calcular participación
    participation_by_course = data.groupby('Curso')['Participación (Sí/No)'].value_counts().unstack()
    participation_by_course.fillna(0, inplace=True)
    
    # Crear gráfico
    st.write("Gráfico de Participación por Curso")
    chart = alt.Chart(participation_by_course.reset_index()).mark_bar().encode(
        x='Curso',
        y=alt.Y('Sí', title='Participación'),
        color=alt.value('steelblue')
    ).properties(width=700)
    st.altair_chart(chart, use_container_width=True)
    
    # Mostrar tabla
    st.write("Tabla de Participación por Curso")
    st.dataframe(participation_by_course)
