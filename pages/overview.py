import streamlit as st

def show(data):
    st.header("Resumen General")
    
    # Indicadores clave
    total_students = data['ID Estudiante'].nunique()
    total_courses = data['Curso'].nunique()
    avg_duration = data['Duración de Conexión (min)'].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Estudiantes", total_students)
    col2.metric("Total de Cursos", total_courses)
    col3.metric("Duración Media de Conexión", f"{avg_duration:.2f} min")
    
    # Mostrar tabla de los primeros datos
    st.write("Vista Previa de los Datos:")
    st.dataframe(data.head())
