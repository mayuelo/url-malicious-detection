import pandas as pd
import joblib
from sklearn.pipeline import Pipeline

# Ruta al modelo guardado
modelo_path = "modelo_svm_pipeline.joblib"
modelo = joblib.load(modelo_path)

# Ruta al CSV de entrada
entrada_path = "entrada.csv"
df_entrada = pd.read_csv(entrada_path)

# Predicciones
predicciones = modelo.predict(df_entrada)

# Guardar resultados
df_resultado = df_entrada.copy()
df_resultado["prediccion"] = predicciones
df_resultado.to_csv("resultado_prediccion.csv", index=False)

print("✅ Predicción completada. Archivo guardado como resultado_prediccion.csv")