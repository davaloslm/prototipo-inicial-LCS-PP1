import pandas as pd
import numpy as np
import random

#random.seed(1)
#np.random.seed(1)

n = 500  # cantidad de envíos simulados

data = {
    "distancia_km": np.random.randint(10, 1000, n),
    "tipo_envio": np.random.choice(["normal", "express"], n),
    "peso_kg": np.round(np.random.uniform(0.5, 50.0, n), 2), #Peso
    "volumen": np.random.randint(100, 50000, n), #dimensiones= alto_cm * ancho_cm * largo_cm
    "es_fragil": np.random.choice([0, 1], n),
    "requiere_frio": np.random.choice([0, 1], n),
    "saturacion_ruta": np.random.randint(1, 11, n),  # 1=libre, 10=saturada
}

df = pd.DataFrame(data)

# Regla para asignar prioridad (lógica de negocio simulada)
def asignar_prioridad(row):
    puntaje = 0
    if row["distancia_km"] > 600:
        puntaje += 3
    elif row["distancia_km"] > 300:
        puntaje += 1

####
    ## Peso y volumen suma
    ## mas peso no recomendable
    if row["peso_kg"] >30.0:
        puntaje += 1
    ## mas tamano menos capasidad para enviar = mas prioritario para enviar
    if row["volumen"] >= 30000:
        puntaje+= 1
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

df["prioridad"] = df.apply(asignar_prioridad, axis=1)
df.to_csv("dataset_envios.csv", index=False)
print(df["prioridad"].value_counts())
print(df.head())