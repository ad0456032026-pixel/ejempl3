# paso 1
codigo = input("ingresa el codigo de rastreo, ejemplo: 2024-tecnologia-sv:  ")

# paso 2
if not codigo:
    print("ERROR: el codigo esta vacio, cerrando el programa...")
elif "-" not in codigo:
    print("error: el formato es invalido, recuerda usar guiones.")
else:
    # paso 3
    inicio = codigo.find("-") + 1
    fin = codigo.rfind("-")

    categoria = codigo[inicio:fin]
    print("la categoria es:", categoria)

    # paso 4
    ruta = "ruta local" if codigo[-2:].upper() == "SV" else "ruta internacional"
    print("tipo de envio:", ruta)
