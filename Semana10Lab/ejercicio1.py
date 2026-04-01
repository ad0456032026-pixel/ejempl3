def transformar_texto(texto, opcion):

    ## Recibe un texto y un número
    ## 1: Mayúsculas, 2: Minúsculas, 3: Capitalizar.

    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return texto


# ejemplo de uso
print(transformar_texto("hola mundo", 1))
