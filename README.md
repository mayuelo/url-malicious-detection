# 🔐 URL Maliciosas - Clasificador SVM

Este repositorio contiene un pipeline completo de Machine Learning para la **detección de URLs maliciosas** utilizando el algoritmo **Support Vector Machine (SVM)**. El objetivo del proyecto es clasificar URLs como benignas, phishing, malware, defacement o spam a partir de características extraídas de cada una.

---

## 📁 Estructura del Proyecto

```
.
├── modelo_svm_pipeline.joblib       # Modelo entrenado exportado (pipeline completo)
├── entrada.csv                      # Dataset de entrada con nuevas URLs a clasificar
├── entrada_preparada.csv           # Dataset corregido con columnas compatibles
├── resultado_final.csv             # Dataset con predicciones del modelo
├── 01_eda_y_pipeline_inicial.ipynb # Notebook con EDA, entrenamiento, evaluación y exportación
├── script_prediccion_externa.py    # Script externo para predicción y exportación
├── requirements.txt                # Dependencias necesarias
└── README.md                       # Este archivo
```

---

## ⚙️ Descripción Técnica

- **Algoritmo usado**: SVM (Support Vector Machine) con `GridSearchCV`.
- **Features de entrada**: más de 70 atributos derivados de las URLs (longitud, entropía, número de dígitos, tokens, etc.).
- **Pipeline**: incluye escalado, selección de features y clasificación.
- **Evaluación**: validación cruzada y matriz de confusión.
- **Exportación**: modelo final guardado con `joblib` y listo para producción.

---

## 🚀 Cómo usar este proyecto

### 1. Clonar repositorio y preparar entorno

```bash
git clone https://github.com/tu_usuario/url-maliciosas-svm.git
cd url-maliciosas-svm
pip install -r requirements.txt
```

### 2. Entrenamiento y evaluación (opcional)

Ejecuta el notebook `01_eda_y_pipeline_inicial.ipynb` para:

- Cargar y analizar el dataset
- Entrenar el modelo
- Validar resultados
- Guardar el modelo como `.joblib`

### 3. Clasificación de nuevas URLs

Coloca tu archivo `entrada.csv` con nuevas URLs (mismo formato que el dataset original), y ejecuta:

```bash
python script_prediccion_externa.py
```

Esto generará:

- `entrada_preparada.csv`: archivo corregido con columnas esperadas
- `resultado_final.csv`: archivo con predicciones agregadas

---

## 📨 Notificaciones automáticas

El pipeline incluye **envío automático de notificaciones por correo** al finalizar el entrenamiento o la predicción (si Gmail está configurado con contraseña de aplicación segura).

---

## 📊 Ejemplo de predicción

```csv
Querylength,domain_token_count,...,Entropy_Afterpath,prediccion
101,3,...,0.678,3
92,2,...,0.442,1
```

La columna `prediccion` contiene la clase estimada (ej: 1 = phishing, 3 = malware, etc.)

---

## 🔒 Consideraciones

- Asegúrate de que las nuevas URLs tengan el mismo esquema de features.
- Si faltan columnas, el sistema las rellena con 0 automáticamente.

---

## ✍️ Autor

Proyecto desarrollado por **Josito** como ejemplo profesional de aplicación de IA en ciberseguridad.

---
