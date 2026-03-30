# LogiTrack 
Sistema web de gestión de envíos logísticos que permite registrar, buscar y hacer seguimiento de paquetes de manera eficiente.
En nuestra plataforma, los operadores pueden crear nuevos envíos con toda la información necesaria, buscar por Tracking ID o destinatario, y consultar el estado de cada paquete en tiempo real.
Además, LogiTrack incorpora un módulo de inteligencia artificial que predice automáticamente la prioridad de cada envío según sus características, optimizando la toma de decisiones logísticas.

## Estructura del Repositorio 📁 


```
prototipo-inicial-LCS-PP1
├─ README.md
├─ docs
│  └─ Informe (Semana 2).pdf
├─ requirements.txt
└─ src
   ├─ backend
   │  ├─ main.py
   │  └─ ml
   │     ├─ entrenar_modelo.py
   │     └─ generar_dataset.py
   ├─ img
   │  └─ logo-logitrack.webp
   └─ prototipo
      ├─ busqueda.html
      ├─ crearEnvio.html
      ├─ index.html
      └─ menu.html
```

## Construido con 🛠️

#### Frontend:
* Lenguaje -> HTML5 + JavaScript
* Framework CSS -> [Bootstrap](https://getbootstrap.com/)
* Íconos -> [Material Symbols](https://fonts.google.com/icons)

#### Backend:
* Lenguaje -> Python
* Framework -> [FastAPI](https://fastapi.tiangolo.com/)
* Servidor -> [Uvicorn](https://www.uvicorn.org/)
* Validación de datos -> [Pydantic](https://docs.pydantic.dev/)
* Mock API  -> [MockAPI.io](https://mockapi.io/)

#### APIs:
* Mock API (envíos)  [MockAPI.io](https://mockapi.io/) 
* API Predictiva (Python)  [Uvicorn + FastAPI](https://fastapi.tiangolo.com/) 

#### Machine Learning:
* Modelo -> Random Forest Classifier
* Librería ML -> [scikit-learn](https://scikit-learn.org/stable/user_guide.html)
* Manipulación de datos -> [Pandas](https://pandas.pydata.org/docs/) + [NumPy](https://numpy.org/doc/stable/)
* Exportación del modelo -> [joblib](https://joblib.readthedocs.io/)

## Módulo de IA — Predicción de Prioridad 

El sistema incluye un modulo de Machine Learning:

1. **Generación del dataset** (`generar_dataset.py`) — Crea 500 envíos simulados con variables como distancia, peso, volumen, tipo de envío, fragilidad, cadena de frío y saturación de ruta. La prioridad se asigna mediante una lógica de puntaje:
   * **Alta** → puntaje ≥ 7
   * **Media** → puntaje entre 3 y 6
   * **Baja** → puntaje ≤ 2

2. **Entrenamiento** (`entrenar_modelo.py`) — Entrena un clasificador Random Forest con 80% de los datos y evalúa con el 20% restante. Exporta el modelo y las columnas de entrenamiento.

3. **API REST** (`main.py`) — Expone el endpoint `POST /predecir-prioridad` que recibe los datos del envío y devuelve la prioridad predicha.

## Despliegue 📦

1. Instala las dependencias de Python:

```bash
pip install -r requirements.txt
```

2. Desde la carpeta raíz del proyecto, ejecuta la API de FastAPI:

```bash
uvicorn src.backend.main:app --reload --host 127.0.0.1 --port 8000
```

3. Abre el navegador para usar el prototipo frontend:

- `src/prototipo/index.html`
- `src/prototipo/crearEnvio.html`
- `src/prototipo/busqueda.html`
- `src/prototipo/menu.html`

## Documentación de la API con Swagger 🧾

- Accede a la UI interactiva en:

```text
http://127.0.0.1:8000/docs
```

- Alternativa en ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Autores ✒️

|   Nombre  |    Rol   |      Contacto      |
| :-------- | :------- | :------------------------- |
| Leonardo Dávalos | Desarrollador | [LinkedIn](https://linkedin.com/in/leonardo-davalos), [GitHub](https://github.com/davaloslm) |
| Grande Federico | Desarrollador | [GitHub](https://github.com/Grande-f) |
| Uribe Tafur, Jamil Alberto | Desarrollador | [LinkedIn](https://www.linkedin.com/), [GitHub](https://github.com/Jamil-Uribe) |