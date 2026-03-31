import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Cargar el dataset que acabamos de inventar
df = pd.read_csv('dataset_envios.csv')

# 2. Preprocesamiento: Convertir texto a números para que el modelo lo entienda
# Transformamos 'tipo_envio' (normal/express) a valores binarios (0 y 1)
df = pd.get_dummies(df, columns=['tipo_envio'], drop_first=True)

# 3. Separar las variables de entrada (X) y la variable a predecir (y)
X = df.drop('prioridad', axis=1) # Todas las columnas menos la prioridad
y = df['prioridad'] # Solo la columna prioridad (Alta, Media, Baja)

# 4. Dividir los datos: 80% para entrenar (aprender) y 20% para probar (evaluar)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Inicializar y Entrenar el Random Forest
modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train) # ¡Aquí es donde ocurre la "magia" del aprendizaje!

# 6. Evaluar el modelo (Requisito E3 del TP)
predicciones = modelo_rf.predict(X_test)
precision = accuracy_score(y_test, predicciones)

print(f"--- Métricas del Prototipo ---")
print(f"Precisión General del Modelo: {precision * 100:.2f}%")
print("\nReporte detallado por clase:")
print(classification_report(y_test, predicciones))

# 7. Guardar el modelo entrenado para usarlo luego en la Mock API
joblib.dump(modelo_rf, 'modelo_prioridad_rf.pkl')
# También guardamos los nombres de las columnas para cuando nos envíen datos nuevos
joblib.dump(X.columns, 'columnas_entrenamiento.pkl')

print("Modelo exportado exitosamente como 'modelo_prioridad_rf.pkl'")