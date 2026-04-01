def transformar_lista(lista_palabras, opcion):

    ###Transforma cada palabra de una lista según la opción seleccionada.

    lista_transformada = []
    for palabra in lista_palabras:
        if opcion == 1:
            lista_transformada.append(palabra.upper())
        elif opcion == 2:
            lista_transformada.append(palabra.lower())
        elif opcion == 3:
            lista_transformada.append(palabra.capitalize())
        else:
            lista_transformada.append(palabra)

    return lista_transformada


# ejemplo:
palabras = ["hOla", "MUNDO", "pyThon"]
print(transformar_lista(palabras, 3))
