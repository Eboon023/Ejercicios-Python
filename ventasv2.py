ventas_validas = []
ventas_invalidas = []

with open('ventas.txt') as archivo:
    for n in archivo:
        try:
            if isinstance(int(n), int) and int(n) >=0 and n != "":
                ventas_validas.append(int(n))
        except:
            ventas_invalidas.append(n.replace('\n', ''))

print(f"Ventas válidas: {ventas_validas}")
print(f"Ventas inválidas: {ventas_invalidas}")
print(f"Total de ventas: {sum(ventas_validas)}")
print(f"Promedio: {sum(ventas_validas) /len(ventas_validas) if ventas_validas else 0}")

archivo.close()