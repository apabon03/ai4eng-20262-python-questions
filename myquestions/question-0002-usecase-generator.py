def generar_caso_de_uso_transformar_tempo_ciclico():
    n = random.randint(10, 20)
    df = pd.DataFrame({'hora': np.random.randint(0, 24, size=n)})
    return df, 'hora'
