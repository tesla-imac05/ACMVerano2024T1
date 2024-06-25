def ordenar_asc(datos):
    arr_len = len(datos)

    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if datos[j] < datos[min_idx]:
                min_idx = j
        datos[i], datos[min_idx] = datos[min_idx], datos[i]

    return datos