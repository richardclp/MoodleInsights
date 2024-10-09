import streamlit as st
from utils.data_loader import load_data

# Cargar datos
data = load_data("data/student_data.csv")

# Configuración del título del dashboard
st.set_page_config(page_title="Educational Dashboard", layout="wide")

# Título y descripción
st.title("Educational Dashboard")
st.sidebar.title("Navegación")

# Menú de navegación
page = st.sidebar.selectbox("Seleccione una sección:", ["Resumen General", "Participación por Curso", "Patrones de Actividad"])

# Condicionales para cargar cada sección
if page == "Resumen General":
    from pages import overview
    overview.show(data)
elif page == "Participación por Curso":
    from pages import course_participation
    course_participation.show(data)
elif page == "Patrones de Actividad":
    from pages import activity_patterns
    activity_patterns.show(data)
