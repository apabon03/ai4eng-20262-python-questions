import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_elasticidad_precio():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función analizar_elasticidad_precio.
    """

    # ---------------------------------------------------------
    # 1. Generar valores válidos para precio y cantidad
    # ---------------------------------------------------------
    
    P1 = round(random.uniform(1, 100), 2)
    P2 = round(random.uniform(1, 100), 2)
    
    Q1 = random.randint(1, 500)
    Q2 = random.randint(1, 500)
    
    # ---------------------------------------------------------
    # 2. Crear DataFrame de entrada
    # ---------------------------------------------------------
    
    df = pd.DataFrame({
        'precio': [P1, P2],
        'cantidad': [Q1, Q2]
    })
    
    input_data = {
        'df_precios': df.copy()
    }
    
    # ---------------------------------------------------------
    # 3. Calcular OUTPUT esperado (Ground Truth)
    # ---------------------------------------------------------
    
    numerador = (Q2 - Q1) / ((Q2 + Q1) / 2)
    denominador = (P2 - P1) / ((P2 + P1) / 2)
    
    if denominador == 0:
        elasticidad = np.inf
    else:
        elasticidad = numerador / denominador
    
    if abs(elasticidad) > 1:
        categoria = "Elástico"
    else:
        categoria = "Inelástico"
    
    output_data = {
        'elasticidad': float(elasticidad),
        'categoria': categoria
    }
    
    return input_data, output_data


# ---------------------------------------------------------
# (Opcional) Ejemplo de uso
# ---------------------------------------------------------
if __name__ == "__main__":
    
    entrada, salida_esperada = generar_caso_de_uso_elasticidad_precio()
    
    print("=== INPUT ===")
    print(entrada['df_precios'])
    
    print("\n=== OUTPUT ESPERADO ===")
    print(salida_esperada)
