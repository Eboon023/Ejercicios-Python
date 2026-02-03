import pandas as pd
df = pd. read_csv("ventas.csv")

total_por_vendedor = {}
ventas_invalidas = []

for _, fila in df.iterrows():
    vendedor = fila["vendedor"]
    monto_raw = fila["monto"]
    if monto_raw == "":
        continue

    try:
        monto = float(monto_raw)
        if monto > 0:
            total_por_vendedor[vendedor] = total_por_vendedor.get(vendedor, 0) + monto
        else:
            ventas_invalidas.append(monto_raw)
    except (ValueError, TypeError):
        ventas_invalidas.append(monto_raw)

print("Total por vendedor:")
for vendedor, total in total_por_vendedor.items():
    print(f"{vendedor}: {total}")