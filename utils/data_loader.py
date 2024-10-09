import pandas as pd

def load_data(filepath):
    # Cargar datos desde el archivo CSV
    data = pd.read_csv(filepath)
    return data
