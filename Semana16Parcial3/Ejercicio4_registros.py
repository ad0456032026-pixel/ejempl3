print("--- inicio de auditoria ---")

for i in range(1, 51):

    if i == 42:
        print("brecha de seguridad detectada. deteniendo proceso...")
        break

    if i % 3 == 0:
        continue

    print(f"procesando registro id: {i}")

print(" auditoria finalizada ")
