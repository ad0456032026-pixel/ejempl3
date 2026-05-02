def sistema_de_notas():
    print("x__Bienvenido al Sistema de Calificaciones__x")

    # 1. Usar WHILE para repetir el ingreso de estudiantes
    continuar = "s"
    while continuar.lower() == "s":

        cantidad_notas = int(input("\n¿Cuántas notas vas a ingresar?: "))
        suma_notas = 0

        # 2. Ingresar calificaciones con FOR
        for i in range(cantidad_notas):
            nota_valida = False

            while not nota_valida:
                nota = float(input(f"Ingresa la nota {i + 1} (del 0 al 10): "))

                # 3. Validar con IF
                if 0 <= nota <= 10:
                    suma_notas += nota
                    nota_valida = True
                else:
                    print("Error: La nota debe estar entre 0 y 10.")

        # Un pequeño if para evitar que el programa falle si el usuario pone 0 notas
        if cantidad_notas > 0:
            promedio = suma_notas / cantidad_notas
            print(f"\nEl promedio es: {promedio:.2f}")

            # 4. Select Case (match-case en Python)
            match promedio:
                case p if 9 <= p <= 10:
                    clasificacion = "Excelente"
                case p if 7 <= p < 9:
                    clasificacion = "Bueno"
                case p if 6 <= p < 7:
                    clasificacion = "Suficiente"
                case p if 0 <= p < 6:
                    clasificacion = "Insuficiente-Reprobado"

            print(f"Clasificación Final: {clasificacion}")
        else:
            print("\nNo ingresaste ninguna nota.")

        print("-" * 45)
        continuar = input("¿Deseas evaluar a otro estudiante? (s/n): ")

    print("\n¡Fin del programa!")


# Aquí llamamos a la función para que el código empiece a ejecutarse
sistema_de_notas()
