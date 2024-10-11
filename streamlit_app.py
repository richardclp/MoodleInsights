import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# Cargar datos desde el archivo CSV
data = pd.read_csv("data/student_data.csv")

# Título del dashboard
st.title("Dashboard de Participación Estudiantil")
# CSS en un string
css_style_menu = """
<style>
[data-testid="stSidebarNav"] {
    padding: 10px;
    background-color: #f8f9fa;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

[data-testid="stSidebarNavItems"] {
    list-style-type: none;
    margin: 0;
    padding: 0;
    font-size: 16px;
}

[data-testid="stSidebarNavItems"] li {
    margin-bottom: 8px;
    border-radius: 10px;
    background-color: #e2e2e2;
    transition: all 0.3s ease;
}

[data-testid="stSidebarNavItems"] li:hover {
    background-color: #b3ecff;
    transform: scale(1.05);
}

[data-testid="stSidebarNavLink"] {
    color: #333;
    text-decoration: none;
    display: block;
    margin: 0;
    border-radius: 8px;
    position: relative;
    transition: all 0.3s ease;
}

[data-testid="stSidebarNavLink"]::before {
    content: '';
    position: absolute;
    left: 0;
    bottom: 0;
    height: 3px;
    width: 0;
    background-color: #007acc;
    transition: width 0.3s ease;
}

[data-testid="stSidebarNavLink"]:hover::before {
    width: 100%;
}

[data-testid="stSidebarNavLink"]:hover {
    color: #007acc;
}

[data-testid="stSidebarNavLink"] span {
    display: inline-block;
    vertical-align: middle;
}
</style>
"""
st.markdown(
    css_style_menu,
    unsafe_allow_html=True,
)

# Mostrar el dataset
st.subheader("Dataset de Participación")
st.dataframe(data)

# Pregunta 1: ¿Cuál es el curso con menor participación?
st.subheader("1. Participación por Curso")
participacion = (
    data.groupby("Curso")["Participación (Sí/No)"].value_counts().unstack().fillna(0)
)

curso_menor_participacion = participacion["No"].idxmax()
curso_mayor_participacion = participacion["No"].idxmin()
menor_participacion_valor = participacion.loc[curso_menor_participacion, "No"]
mayor_participacion_valor = participacion.loc[curso_mayor_participacion, "Sí"]

# Crear columnas para mostrar métricas
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Curso con Mayor Participación",
        value=curso_mayor_participacion,
        delta=int(mayor_participacion_valor),
    )

with col2:
    st.metric(
        label="Curso con Menor Participación",
        value=curso_menor_participacion,
        delta=int(menor_participacion_valor),
        delta_color="inverse",
    )


# ----------------------------------------------------------------
# Gráfico de participación por curso
# plt.figure(figsize=(10, 5))
# sns.countplot(data=data, x="Curso", hue="Participación (Sí/No)", palette="Set2")
# plt.title("Participación por Curso")
# plt.xlabel("Curso")
# plt.ylabel("Número de Estudiantes")
# st.pyplot(plt)
# plt.close()  # Cerrar el gráfico para evitar superposición
# ----------------------------------------------------------------
# Calcular la cantidad de estudiantes por curso y participación
participacionEst = (
    data.groupby(["Curso", "Participación (Sí/No)"])["ID Estudiante"]
    .count()
    .reset_index()
)
participacionEst.columns = ["Curso", "Participación", "Cantidad"]

# Crear el gráfico de barras agrupadas
chart = (
    alt.Chart(participacionEst)
    .mark_bar()
    .encode(
        x=alt.X("Curso:N", title="Curso", axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("Cantidad:Q", title="Número de Estudiantes"),
        color=alt.Color(
            "Participación:N", scale=alt.Scale(scheme="set2"), title="Participación"
        ),
        column=alt.Column("Participación:N", title="Participación"),
    )
    .properties(width=alt.Step(50))  # Ajusta el ancho del gráfico según lo necesites
    .configure_axis(labelFontSize=12, titleFontSize=14)
    .configure_legend(titleFontSize=14, labelFontSize=12)
)

# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)
# ----------------------------------------------------------------

# Pregunta 2: ¿En qué horario están más activos los estudiantes?
st.subheader("2. Horario de mayor actividad")
data["Hora de Conexión"] = pd.to_datetime(
    data["Hora de Conexión"], format="%H:%M"
).dt.hour
hora_actividad = data["Hora de Conexión"].value_counts().sort_index()

# Calcular las dos horas con más actividad
top_horas_actividad = hora_actividad.nlargest(2)

# Crear columnas para mostrar las dos horas con mayor actividad
col1, col2 = st.columns(2)

# Métricas para las dos horas con más actividad
col1.metric(
    label="Hora con Más Actividad",
    value=f"{top_horas_actividad.index[0]}:00",
    delta=int(top_horas_actividad.iloc[0]),
)
col2.metric(
    label="Segunda Hora con Más Actividad",
    value=f"{top_horas_actividad.index[1]}:00",
    delta=int(top_horas_actividad.iloc[1]),
)

# Mostrar gráfico de la actividad por hora
st.bar_chart(hora_actividad)

# Graficar la hora de actividad
# plt.figure(figsize=(10, 5))
# plt.bar(hora_actividad.index, hora_actividad.values, color="skyblue")
# plt.title("Horario de Mayor Actividad")
# plt.xlabel("Hora de Conexión")
# plt.ylabel("Número de Conexiones")
# plt.xticks(hora_actividad.index)  # Mostrar cada hora en el eje x

# Anotar los valores exactos en las barras
# for index, value in enumerate(hora_actividad.values):
#    plt.text(hora_actividad.index[index], value + 0.2, str(value), ha="center")

# st.pyplot(plt)
# plt.close()  # Cerrar el gráfico para evitar superposición

# Pregunta 3: Estudiantes más activos
st.subheader("3. Estudiantes más activos")
top_duracion = (
    data.groupby("ID Estudiante")["Duración de Conexión (min)"]
    .sum()
    .sort_values(ascending=False)
)

# Mostrar la lista de estudiantes con mayor duración de conexión
st.write("**Estudiantes con mayor duración de conexión:**")
st.write(top_duracion)

# Filtrar el top 10 de estudiantes más activos
top_10_duracion = top_duracion.head(10)

# Crear gráfico de barras para el top 10
st.bar_chart(top_10_duracion)

# plt.figure(figsize=(10, 6))
# top_10_duracion.plot(kind="bar", color="skyblue")
# lt.title("Top 10 Estudiantes con Mayor Duración de Conexión")
# plt.xlabel("ID Estudiante")
# plt.ylabel("Duración de Conexión (min)")
# st.pyplot(plt)


# Pregunta 4: Comparación de Cursos (Matemáticas vs Biología)
st.subheader("4. Comparación de Cursos (Matemáticas vs Biología)")
comparacion = data[data["Curso"].isin(["Matemáticas", "Biología"])]

# Calcular estadísticas para Matemáticas y Biología
matematicas_stats = comparacion[comparacion["Curso"] == "Matemáticas"][
    "Duración de Conexión (min)"
].describe()
biologia_stats = comparacion[comparacion["Curso"] == "Biología"][
    "Duración de Conexión (min)"
].describe()

# Crear dos columnas para mostrar las estadísticas una al lado de la otra
col1, col2 = st.columns(2)

with col1:
    st.write("**Estadísticas de Matemáticas**")
    st.write(matematicas_stats)

with col2:
    st.write("**Estadísticas de Biología**")
    st.write(biologia_stats)

# Gráfico de comparación
plt.figure(figsize=(10, 5))
sns.boxplot(x="Curso", y="Duración de Conexión (min)", data=comparacion)
plt.title("Comparación de Duración de Conexión")
st.pyplot(plt)
plt.close()  # Cerrar el gráfico para evitar superposición

# Reflexión Final
# st.subheader("Reflexión Final")
# st.write(
#    "¿Qué acciones podrían tomar los docentes para aumentar la participación en los cursos con menor actividad?"
# )
