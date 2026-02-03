ventas_validas = []
ventas_invalidas = []

with open("ventas.txt", encoding="utf-8") as archivo:
    for linea in archivo:
        valor = linea.strip()

        if valor == "":
            continue

        try:
            monto = float(valor)
            if monto > 0:
                ventas_validas.append(monto)
            else:
                ventas_invalidas.append(valor)
        except (ValueError, TypeError):
            ventas_invalidas.append(valor)

total = sum(ventas_validas)
promedio = total / len(ventas_validas) if ventas_validas else 0

print(f"Ventas válidas: {ventas_validas}")
print(f"Ventas inválidas: {ventas_invalidas}")
print(f"Total de ventas: {total}")
print(f"Promedio: {promedio}")
