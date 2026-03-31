import requests
import pytest

URL = "http://127.0.0.1:8000/predecir-prioridad"


@pytest.mark.parametrize(
    "envio, prioridad_esperada",
    [
        pytest.param(
            {
                "distancia_km": 750,
                "tipo_envio": "express",
                "peso_kg": 35.0,
                "volumen": 40000,
                "es_fragil": 0,
                "requiere_frio": 0,
                "saturacion_ruta": 3,
            },
            "Alta",
            id="alta_express_pesado_voluminoso",
        ),
        pytest.param(
            {
                "distancia_km": 400,
                "tipo_envio": "normal",
                "peso_kg": 8.0,
                "volumen": 2000,
                "es_fragil": 1,
                "requiere_frio": 1,
                "saturacion_ruta": 7,
            },
            "Media",
            id="media_fragil_frio_saturacion_media",
        ),
        pytest.param(
            {
                "distancia_km": 150,
                "tipo_envio": "express",
                "peso_kg": 5.0,
                "volumen": 500,
                "es_fragil": 1,
                "requiere_frio": 0,
                "saturacion_ruta": 2,
            },
            "Media",
            id="media_express_corta_distancia",
        ),
        pytest.param(
            {
                "distancia_km": 200,
                "tipo_envio": "normal",
                "peso_kg": 15.0,
                "volumen": 8000,
                "es_fragil": 0,
                "requiere_frio": 1,
                "saturacion_ruta": 3,
            },
            "Baja",
            id="baja_normal_distancia_media_sin_saturacion",
        ),
        pytest.param(
            {
                "distancia_km": 50,
                "tipo_envio": "normal",
                "peso_kg": 2.0,
                "volumen": 300,
                "es_fragil": 0,
                "requiere_frio": 0,
                "saturacion_ruta": 1,
            },
            "Baja",
            id="baja_todo_minimo",
        ),
    ],
)

def test_prediccion_prioridad(envio, prioridad_esperada):

    response = requests.post(URL, json=envio)

    assert response.status_code == 200

    data = response.json()

    assert data["estado"] == "exito"

    assert data["prioridad_asignada"] == prioridad_esperada