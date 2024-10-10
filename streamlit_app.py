import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos desde el archivo CSV
data = pd.read_csv("data/student_data.csv")

# Título del dashboard
st.title("Dashboard de Participación Estudiantil")

# Mostrar el dataset
st.subheader("Dataset de Participación")
st.dataframe(data)

# Pregunta 1: ¿Cuál es el curso con menor participación?
st.subheader("1. Curso con menor participación")
participacion = (
    data.groupby("Curso")["Participación (Sí/No)"].value_counts().unstack().fillna(0)
)
curso_menor_participacion = participacion["No"].idxmax()

st.write(f"**Curso con menor participación:** {curso_menor_participacion}")

# Gráfico de participación por curso
plt.figure(figsize=(10, 5))
sns.countplot(data=data, x="Curso", hue="Participación (Sí/No)", palette="Set2")
plt.title("Participación por Curso")
plt.xlabel("Curso")
plt.ylabel("Número de Estudiantes")
st.pyplot(plt)
plt.close()  # Cerrar el gráfico para evitar superposición

# Pregunta 2: ¿En qué horario están más activos los estudiantes?
st.subheader("2. Horario de mayor actividad")
data["Hora de Conexión"] = pd.to_datetime(
    data["Hora de Conexión"], format="%H:%M"
).dt.hour
hora_actividad = data["Hora de Conexión"].value_counts().sort_index()

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

st.write("**Estudiantes con mayor duración de conexión:**")
st.write(top_duracion)

# Pregunta 4: Comparación de cursos
st.subheader("4. Comparación de Cursos (Matemáticas vs Biología)")
comparacion = data[data["Curso"].isin(["Matemáticas", "Biología"])]
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
