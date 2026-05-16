temperaturas = []

print(" sensor industrial")

for i in range(5):
    lectura = int(input(f"ingresa la temperatura {i+1} de 5: "))

    temperaturas.append(lectura)

print("\n--- resultados del analisis ---")

for t in temperaturas:
    match t:
        case 0:
            print(f"[{t}°c] alerta: punto de congelacion")
        case 100:
            print(f"[{t}°c] alerta: punto de ebullicion")
        case _:
            estado = "estado: estable" if 10 <= t <= 30 else "estado: critico"
            print(f"[{t}°c] {estado}")
