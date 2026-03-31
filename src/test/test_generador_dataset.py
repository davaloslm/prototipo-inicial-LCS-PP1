
import pytest
import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'ml')))

from generar_dataset import asignar_prioridad

@pytest.fixture(scope="module")
def dataset():
    np.random.seed(1)
    n = 500
    data = {
        "distancia_km":   np.random.randint(10, 1000, n),
        "tipo_envio":     np.random.choice(["normal", "express"], n),
        "peso_kg":        np.round(np.random.uniform(0.5, 50.0, n), 2),
        "volumen":        np.random.randint(100, 50000, n),
        "es_fragil":      np.random.choice([0, 1], n),
        "requiere_frio":  np.random.choice([0, 1], n),
        "saturacion_ruta": np.random.randint(1, 11, n),
    }
    df = pd.DataFrame(data)
    df["prioridad"] = df.apply(asignar_prioridad, axis=1)
    return df


class TestValoresDataset:

    # distancia_km
    def test_distancia_km_minimo(self, dataset):
        """distancia_km >= 10 """
        assert (dataset["distancia_km"] >= 10).all(), \
            f"Hay valores menores a 10: {dataset[dataset['distancia_km'] < 10]['distancia_km'].tolist()}"

    def test_distancia_km_maximo(self, dataset):
        """distancia_km < 1000 """
        assert (dataset["distancia_km"] < 1000).all(), \
            f"Hay valores >= 1000: {dataset[dataset['distancia_km'] >= 1000]['distancia_km'].tolist()}"

    def test_distancia_km_es_entero(self, dataset):
        """distancia_km debe ser número entero."""
        assert dataset["distancia_km"].dtype in [np.int32, np.int64]

    # tipo_envio
    def test_tipo_envio_solo_valores_validos(self, dataset):
        """tipo_envio solo puede ser 'normal' o 'express'."""
        valores_invalidos = set(dataset["tipo_envio"].unique()) - {"normal", "express"}
        assert not valores_invalidos, f"Valores inesperados: {valores_invalidos}"

    def test_tipo_envio_ambas_categorias_presentes(self, dataset):
        """Con 500 registros deben aparecer tanto 'normal' como 'express'."""
        assert "normal" in dataset["tipo_envio"].values
        assert "express" in dataset["tipo_envio"].values

    # peso_kg y volumen
    def test_peso_kg_minimo(self, dataset):
        """peso_kg >= 0.5 (np.random.uniform(0.5, 50.0))."""
        assert (dataset["peso_kg"] >= 0.5).all(), \
            f"Hay pesos menores a 0.5: {dataset[dataset['peso_kg'] < 0.5]['peso_kg'].tolist()}"

    def test_peso_kg_maximo(self, dataset):
        """peso_kg <= 50.0 (límite de uniform)."""
        assert (dataset["peso_kg"] <= 50.0).all(), \
            f"Hay pesos mayores a 50: {dataset[dataset['peso_kg'] > 50]['peso_kg'].tolist()}"

    def test_peso_kg_dos_decimales(self, dataset):
        """peso_kg tiene como máximo 2 decimales (np.round(..., 2))."""
        decimales = (dataset["peso_kg"] * 100).round(0) / 100
        assert (decimales == dataset["peso_kg"]).all()

    def test_volumen_minimo(self, dataset):
        """volumen >= 100 (np.random.randint(100, 50000))."""
        assert (dataset["volumen"] >= 100).all(), \
            f"Hay volúmenes menores a 100: {dataset[dataset['volumen'] < 100]['volumen'].tolist()}"

    def test_volumen_maximo(self, dataset):
        """volumen < 50000 (límite exclusivo de randint)."""
        assert (dataset["volumen"] < 50000).all(), \
            f"Hay volúmenes >= 50000: {dataset[dataset['volumen'] >= 50000]['volumen'].tolist()}"

    def test_volumen_es_entero(self, dataset):
        """volumen debe ser número entero."""
        assert dataset["volumen"].dtype in [np.int32, np.int64]

    # es_fragil y requiere_frio
    def test_es_fragil_solo_0_y_1(self, dataset):
        """es_fragil solo puede ser 0 o 1."""
        valores_invalidos = set(dataset["es_fragil"].unique()) - {0, 1}
        assert not valores_invalidos, f"Valores inesperados: {valores_invalidos}"

    def test_es_fragil_ambos_valores_presentes(self, dataset):
        """Con 500 registros deben aparecer tanto 0 como 1."""
        assert 0 in dataset["es_fragil"].values
        assert 1 in dataset["es_fragil"].values

    def test_requiere_frio_solo_0_y_1(self, dataset):
        """requiere_frio solo puede ser 0 o 1."""
        valores_invalidos = set(dataset["requiere_frio"].unique()) - {0, 1}
        assert not valores_invalidos, f"Valores inesperados: {valores_invalidos}"

    def test_requiere_frio_ambos_valores_presentes(self, dataset):
        """Con 500 registros deben aparecer tanto 0 como 1."""
        assert 0 in dataset["requiere_frio"].values
        assert 1 in dataset["requiere_frio"].values

    # saturacion_ruta
    def test_saturacion_ruta_minimo(self, dataset):
        """saturacion_ruta >= 1 (np.random.randint(1, 11))."""
        assert (dataset["saturacion_ruta"] >= 1).all(), \
            f"Hay valores menores a 1: {dataset[dataset['saturacion_ruta'] < 1]['saturacion_ruta'].tolist()}"

    def test_saturacion_ruta_maximo(self, dataset):
        """saturacion_ruta <= 10 (límite exclusivo de randint(1, 11))."""
        assert (dataset["saturacion_ruta"] <= 10).all(), \
            f"Hay valores mayores a 10: {dataset[dataset['saturacion_ruta'] > 10]['saturacion_ruta'].tolist()}"

    def test_saturacion_ruta_es_entero(self, dataset):
        """saturacion_ruta debe ser número entero."""
        assert dataset["saturacion_ruta"].dtype in [np.int32, np.int64]

    def test_saturacion_ruta_todos_los_niveles(self, dataset):
        """Con 500 registros deben aparecer los 10 niveles de saturación."""
        niveles_presentes = set(dataset["saturacion_ruta"].unique())
        niveles_esperados = set(range(1, 11))
        assert niveles_esperados == niveles_presentes, \
            f"Niveles faltantes: {niveles_esperados - niveles_presentes}"

    # prioridad
    def test_prioridad_solo_valores_validos(self, dataset):
        """prioridad solo puede ser 'Alta', 'Media' o 'Baja'."""
        valores_invalidos = set(dataset["prioridad"].unique()) - {"Alta", "Media", "Baja"}
        assert not valores_invalidos, f"Valores inesperados: {valores_invalidos}"

    def test_prioridad_tres_clases_presentes(self, dataset):
        """Con 500 registros deben existir las tres clases."""
        assert set(dataset["prioridad"].unique()) == {"Alta", "Media", "Baja"}


    def test_sin_valores_nulos(self, dataset):
        """El dataset no debe tener ningún valor nulo en ninguna columna."""
        nulos = dataset.isnull().sum()
        columnas_con_nulos = nulos[nulos > 0].to_dict()
        assert not columnas_con_nulos, f"Columnas con nulos: {columnas_con_nulos}"

    def test_cantidad_de_columnas(self, dataset):
        """El dataset debe tener exactamente 8 columnas."""
        assert len(dataset.columns) == 8

