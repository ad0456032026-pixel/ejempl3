def transformar_con_validacion(texto, opcion):

    ### Muestra 'opción inválida' si el número no es 1, 2 o 3.

    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        print("Opción inválida")
        return None


# Ejemplo de uso:
transformar_con_validacion("texto de prueba", 5)
