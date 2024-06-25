def format_str(datos):
    d_formated = []
    for dato in datos:
        if isinstance(dato, str):
            dato_formateado = dato.upper().replace(" ", "")
            d_formated.append(dato_formateado)
        else:
            d_formated.append(dato)
    return d_formated