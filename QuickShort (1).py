# Función para intercambiar valores
def intercambiar(arreglo, i, j):
    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

# Función de partición
def particion(arreglo, inicio, fin):
    pivote = arreglo[fin]  # Tomamos el último elemento como pivote
    i = inicio - 1

    for j in range(inicio, fin):
        if arreglo[j] < pivote:
            i += 1
            intercambiar(arreglo, i, j)
    
    intercambiar(arreglo, i + 1, fin)
    return i + 1

# Función QuickSort
def quickSort(arreglo, inicio, fin):
    if inicio < fin:
        indicePivote = particion(arreglo, inicio, fin)

        # Ordenamos recursivamente los elementos a la izquierda y derecha del pivote
        quickSort(arreglo, inicio, indicePivote - 1)
        quickSort(arreglo, indicePivote + 1, fin)

# Programa principal
def main():
    n = int(input("Cuantos elementos quieres ordenar? "))
    arreglo = []

    print(f"Ingresa los {n} elementos:")
    for _ in range(n):
        num = int(input())
        arreglo.append(num)

    quickSort(arreglo, 0, n - 1)

    print("Arreglo ordenado:", arreglo)

if __name__ == "__main__":
    main()