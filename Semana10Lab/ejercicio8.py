def transformar_opcion(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    return texto


def menu_principal():
    while True:
        print("\n--- MENÚ DE TRANSFORMACIÓN DE TEXTO ---")
        print("1. Convertir todo a mayúsculas")
        print("2. Convertir todo a minúsculas")
        print("3. Colocar la primera letra en mayúscula")
        print("4. Salir")

        opcion_str = input("Elige una opción (1-4): ")

        if opcion_str == "4":
            print("Saliendo del programa...")
            break

        if opcion_str in ["1", "2", "3"]:
            texto = input("Ingresa el texto a transformar: ")
            opcion = int(opcion_str)
            resultado = transformar_opcion(texto, opcion)
            print(f"-> Resultado: {resultado}")
        else:
            print("-> Opción inválida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
