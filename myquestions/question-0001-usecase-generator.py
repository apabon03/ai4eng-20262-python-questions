import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_analizar_elasticidad_precio():
    p1 = random.uniform(10.0, 100.0)
    p2 = p1 * random.uniform(0.7, 1.3)
    q1 = random.randint(500, 1000)
    q2 = q1 * random.uniform(0.5, 1.5)
    return pd.DataFrame({'precio': [p1, p2], 'cantidad': [q1, q2]})
