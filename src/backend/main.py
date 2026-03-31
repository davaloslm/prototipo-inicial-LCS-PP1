from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

# 1. Inicializar la aplicación FastAPI
app = FastAPI(
    title="API Predictiva - LogiTrack",
    description="Microservicio para calcular la prioridad de envíos logísticos usando Random Forest.",
    version="1.0.0"
)

# 2. Cargar el modelo entrenado y las columnas esperadas al arrancar el servidor
try:
    modelo_rf = joblib.load('src/backend/ml/modelo_prioridad_rf.pkl')
    columnas_entrenamiento = joblib.load('src/backend/ml/columnas_entrenamiento.pkl')
    print("Modelo de IA cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}. Asegúrate de haber ejecutado el entrenamiento.")

# 3. Definir el esquema de datos que la API espera recibir usando Pydantic
class DatosEnvio(BaseModel):
    distancia_km: float = Field(..., description="Distancia estimada en km")
    tipo_envio: str = Field(..., description="'normal' o 'express'")
    peso_kg: float = Field(..., description="Peso del paquete en kg")
    volumen: float = Field(..., description="Volumen en cm³")
    es_fragil: int = Field(..., description="1 = frágil, 0 = no frágil")
    requiere_frio: int = Field(..., description="1 = requiere cadena de frío, 0 = no")
    saturacion_ruta: int = Field(..., description="Nivel de saturación de la ruta (1-10)")

# 4. Crear el endpoint (Ruta) que recibe los datos y devuelve la predicción
@app.post("/predecir-prioridad", summary="Calcula la prioridad de un envío")
def predecir_prioridad(envio: DatosEnvio):
    try:
        # A. Convertir los datos recibidos (JSON) a un formato que Pandas entienda (DataFrame)
        df_entrada = pd.DataFrame([envio.dict()])

        # B. Aplicar el mismo preprocesamiento que usamos en el entrenamiento (get_dummies)
        df_entrada = pd.get_dummies(df_entrada, columns=['tipo_envio'])

        # C. Alinear las columnas con las del modelo original
        # Esto es crucial: si el modelo se entrenó con 'tipo_envio_express',
        # esta línea asegura que la columna exista, rellenando con 0 si es necesario.
        df_entrada = df_entrada.reindex(columns=columnas_entrenamiento, fill_value=0)

        # D. Realizar la predicción
        prediccion = modelo_rf.predict(df_entrada)[0]

        # E. Devolver el resultado
        return {
            "estado": "exito",
            "prioridad_asignada": prediccion,
            "mensaje": f"El envío ha sido clasificado con prioridad {prediccion}."
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la predicción: {str(e)}")