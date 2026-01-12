array_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Recorrido inicial:")
for i, numero in enumerate(array_numeros):
    print(f"[{i}]: {numero}")

print("Buscando el valor 8:")
for i, numero in enumerate(array_numeros):
    if numero == 8:
        print(f"¡Encontrado! El valor 8 está en la posición {i}")
        break

array_numeros.insert(5, 22)

print("Recorrido después de la inserción:")
for i, numero in enumerate(array_numeros):
    print(f"[{i}]: {numero}")

print("Recorrido inverso:")
for i, numero in enumerate(reversed(array_numeros)):
    print(f"[{len(array_numeros)-1-i}]: {numero}")