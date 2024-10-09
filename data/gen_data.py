import pandas as pd
import random
import numpy as np

# Configuración de semilla para reproducibilidad
random.seed(0)
np.random.seed(0)

# Generar datos simulados
num_records = 500

# Simulación de datos
data = {
    "ID Estudiante": [f"E{str(i).zfill(3)}" for i in range(1, num_records + 1)],
    "Curso": random.choices(["Matemáticas", "Historia", "Biología", "Química", "Inglés", "Física", "Arte", "Computación"], k=num_records),
    "Participación (Sí/No)": random.choices(["Sí", "No"], weights=[0.7, 0.3], k=num_records),
    "Duración de Conexión (min)": np.random.randint(5, 120, size=num_records),
    "Hora de Conexión": [f"{random.randint(6, 23)}:{str(random.randint(0, 59)).zfill(2)}" for _ in range(num_records)]
}

# Crear DataFrame
student_data_df = pd.DataFrame(data)

# Mostrar las primeras filas
student_data_df.head(), student_data_df.shape
