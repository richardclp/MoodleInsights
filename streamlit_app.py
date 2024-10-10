import streamlit as st
from utils.data_loader import load_data

# Cargar datos
data = load_data("data/student_data.csv")

# Configuración del título del dashboard
st.set_page_config(page_title="Educational Dashboard", layout="wide")

# Título y descripción
st.title("Educational Dashboard")

# Opciones de navegación
pages = ["Resumen General", "Participación por Curso", "Patrones de Actividad"]

# Menú desplegable en el cuerpo principal
selected_page = st.selectbox("Seleccione una sección:", pages)

# Menú lateral que refleja el valor del combo seleccionado
sidebar_page = st.sidebar.radio("Navegación", pages, index=pages.index(selected_page))

# Sincronizar la página seleccionada en el menú principal con el menú lateral
if selected_page != sidebar_page:
    selected_page = sidebar_page

# Condicionales para cargar cada sección
if selected_page == "Resumen General":
    from pages import overview

    overview.show(data)
elif selected_page == "Participación por Curso":
    from pages import course_participation

    course_participation.show(data)
elif selected_page == "Patrones de Actividad":
    from pages import activity_patterns

    activity_patterns.show(data)
