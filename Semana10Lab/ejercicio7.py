def aplicar_multiples_transformaciones(texto, lista_opciones):

    ### Aplica una lista de transformaciones en orden y devuelve el resultado.

    resultado = texto
    for opcion in lista_opciones:
        if opcion == 1:
            resultado = resultado.upper()
        elif opcion == 2:
            resultado = resultado.lower()
        elif opcion == 3:
            resultado = resultado.capitalize()

    return resultado


# Ejemplo de uso:
print(aplicar_multiples_transformaciones("pYtHoN", [1, 2, 3]))
