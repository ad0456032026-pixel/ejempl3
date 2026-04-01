def mostrar_transformacion(palabra, opcion):

    ## Recibe una palabra y un número, y muestra el resultado en pantalla.

    if opcion == 1:
        resultado = palabra.upper()
    elif opcion == 2:
        resultado = palabra.lower()
    elif opcion == 3:
        resultado = palabra.capitalize()
    else:
        resultado = palabra

    print(resultado)


# ejemplo
mostrar_transformacion("Python", 2)
