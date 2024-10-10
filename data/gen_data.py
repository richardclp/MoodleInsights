import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Configuración de semilla para reproducibilidad
# random.seed(0)
# np.random.seed(0)

# Definir el número de estudiantes y las materias
num_students = 78
courses = [
    "Matemáticas",
    "Historia",
    "Biología",
    "Química",
    "Inglés",
    "Física",
    "Arte",
    "Computación",
]

# Simulación de datos
data = []

for student_id in range(1, num_students + 1):
    # Generar datos para cada curso del estudiante
    for course in courses:
        record = {
            "ID Estudiante": f"E{str(student_id).zfill(3)}",
            "Curso": course,
            "Participación (Sí/No)": random.choices(
                ["Sí", "No"], weights=[0.7, 0.3], k=1
            )[0],
            "Duración de Conexión (min)": np.random.randint(5, 120),
            "Hora de Conexión": f"{random.randint(6, 23)}:{str(random.randint(0, 59)).zfill(2)}",
            # columna de Fecha aleatoria con 30 días hacia atrás
            "Fecha": (datetime.now() - timedelta(days=random.randint(0, 30))).date(),
            # columna de Tareas Completadas
            "Tareas Completadas": np.random.randint(0, 4),  # Entre 0 y 3
        }
        data.append(record)

# Crear DataFrame
student_data_df = pd.DataFrame(data)

# Mostrar las primeras filas
print(student_data_df.head())

# Guardar el DataFrame en un archivo CSV
student_data_df.to_csv("./data/student_data.csv", index=False, encoding="utf-8")

# Guardar el DataFrame en un archivo Excel
student_data_df.to_excel("./data/student_data.xlsx", index=False, engine="openpyxl")

# Mostrar la forma del DataFrame
print(student_data_df.shape)
