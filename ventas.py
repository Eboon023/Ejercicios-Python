ventas = [100, 200, -50, "300", None, 400]
ventas_validas = []
ventas_invalidas = []

for n in ventas:
    if isinstance(n, int) and n >=0:
        ventas_validas.append(n)
    else:
        ventas_invalidas.append(n)



print(f"Las ventas validas son: {ventas_validas}")
print(f"El total de ventas es: {sum(ventas_validas)}")
print(f"El promedio de ventas es: {sum(ventas_validas)/len(ventas_validas)}")
print(ventas_invalidas)