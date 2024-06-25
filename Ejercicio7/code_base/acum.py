def calcular_frecuencias_acumuladas(frecuencias_clase):
    frecuencias_acumuladas = []
    acumulado = 0
    for frec in frecuencias_clase:
        acumulado += frec
        frecuencias_acumuladas.append(acumulado)
    return frecuencias_acumuladas