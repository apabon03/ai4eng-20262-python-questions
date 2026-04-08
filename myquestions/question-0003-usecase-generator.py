import pandas as pd
import numpy as np
import random

from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def generar_caso_modelo_stacking():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función treinar_modelo_stacking.
    """
    
    # ---------------------------------------------------------
    # 1. Configuración aleatoria
    # ---------------------------------------------------------
    
    n_rows = random.randint(20, 100)      # más datos para que el modelo tenga sentido
    n_features = random.randint(2, 6)
    
    # ---------------------------------------------------------
    # 2. Generar datos aleatorios
    # ---------------------------------------------------------
    
    X = np.random.randn(n_rows, n_features)
    
    # Target binario (clasificación)
    y = np.random.randint(0, 2, size=n_rows)
    
    # Opcional: convertir a DataFrame para hacerlo más retador
    if random.choice([True, False]):
        feature_cols = [f'feature_{i}' for i in range(n_features)]
        X = pd.DataFrame(X, columns=feature_cols)
    
    # ---------------------------------------------------------
    # 3. Construir INPUT
    # ---------------------------------------------------------
    
    input_data = {
        'X': X.copy(),
        'y': y.copy()
    }
    
    # ---------------------------------------------------------
    # 4. Calcular OUTPUT esperado (Ground Truth)
    # ---------------------------------------------------------
    
    # Definir estimadores base
    estimators = [
        ('rf', RandomForestClassifier()),
        ('knn', KNeighborsClassifier())
    ]
    
    # Definir modelo de stacking
    modelo = StackingClassifier(
        estimators=estimators,
        final_estimator=LogisticRegression()
    )
    
    # Entrenar modelo
    modelo.fit(X, y)
    
    output_data = modelo
    
    return input_data, output_data


# ---------------------------------------------------------
# Ejemplo de uso
# ---------------------------------------------------------
if __name__ == "__main__":
    
    entrada, salida_esperada = generar_caso_modelo_stacking()
    
    print("=== INPUT ===")
    print(f"Shape de X: {entrada['X'].shape}")
    print(f"Shape de y: {entrada['y'].shape}")
    
    print("\n=== OUTPUT ESPERADO ===")
    print(type(salida_esperada))
    print("Modelo entrenado correctamente ✔")
