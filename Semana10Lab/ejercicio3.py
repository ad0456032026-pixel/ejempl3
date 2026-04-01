def aplicar_transformacion(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    return texto


if __name__ == "__main__":
    texto_usuario = input("Ingresa un texto: ")
    try:
        opcion_usuario = int(
            input("Ingresa un número (1: Mayúsculas, 2: Minúsculas, 3: Capitalizar): ")
        )
        resultado = aplicar_transformacion(texto_usuario, opcion_usuario)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Debes ingresar un número válido.")
