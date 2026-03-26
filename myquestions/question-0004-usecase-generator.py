from sklearn.datasets import make_classification

def generar_caso_de_uso_treinar_modelo_stacking():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=random.randint(1, 1000))
    return X, y
