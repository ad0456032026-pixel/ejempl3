def contar_caracteres_transformados(texto, opcion):

    ### Transforma el texto y devuelve la cantidad de caracteres del resultado.

    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        resultado = texto

    return len(resultado)


# Ejemplo de uso:
print(contar_caracteres_transformados("Hola", 1))
