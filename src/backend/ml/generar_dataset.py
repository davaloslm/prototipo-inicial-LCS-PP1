import pandas as pd
import numpy as np
# import random

# Definimos la cantidad de envíos simulados
num_envios = 500

# Generamos datos aleatorios para las features requeridas
data = {
    "distancia_km": np.random.randint(10, 1000, num_envios),
    "tipo_envio": np.random.choice(["normal", "express"], num_envios),
    "peso_kg": np.round(np.random.uniform(0.5, 50.0, num_envios), 2), # Peso
    "volumen": np.random.randint(100, 50000, num_envios), # dimensiones= alto_cm * ancho_cm * largo_cm
    "es_fragil": np.random.choice([0, 1], num_envios),
    "requiere_frio": np.random.choice([0, 1], num_envios),
    "saturacion_ruta": np.random.randint(1, 11, num_envios),  # 1=libre, 10=saturada
}

df = pd.DataFrame(data)

# Función lógica para asignar la prioridad y que el modelo tenga algo que "aprender"
# Regla para asignar prioridad (lógica de negocio simulada)
def asignar_prioridad(row):
    puntaje = 0
    if row["distancia_km"] > 600:
        puntaje += 3
    elif row["distancia_km"] > 300:
        puntaje += 1

####
    # Peso y volumen suma
    # mas peso no recomendable
    if row["peso_kg"] > 30.0:
        puntaje += 1
    # mas tamano menos capasidad para enviar = mas prioritario para enviar
    if row["volumen"] >= 30000:
        puntaje += 1
####

    if row["tipo_envio"] == "express":
        puntaje += 3

    if row["es_fragil"] == 1:
        puntaje += 1

    if row["requiere_frio"] == 1:
        puntaje += 1

    if row["saturacion_ruta"] >= 7:
        puntaje += 2

    if puntaje >= 7:
        return "Alta"
    elif puntaje >= 3:
        return "Media"
    else:
        return "Baja"
    # El puntaje se basa en:
    # -Alta si tiene 7 o más
    # -Media si tiene entre 3 y 5 puntos
    # -Baja si tiene menos o igual que 2 puntos

# Aplicamos la lógica para crear la columna objetivo (Target)
df['prioridad'] = df.apply(asignar_prioridad, axis=1)

# Guardamos el dataset inventado en un CSV
df.to_csv('dataset_envios.csv', index=False)
print("¡Dataset generado con éxito en 'dataset_envios.csv'!")

print(df["prioridad"].value_counts())
print(df.head())
