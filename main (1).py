#Eliminar duplicados
print("*******ELIMINAR DUPLICADOS*******")

unadim = [1, 2, 2, 3, 4, 4, 5]
print("Matriz original:")
print(unadim)

sinduplicados = list(set(unadim))

print("Eliminar duplicados: ")
print(sinduplicados)

#Ordenar por filas
print("\n*******ORDENAR POR FILAS*******")
import numpy as np
dosdim = np.array([[10, 9, 0],
                   [1, 5, 3],
                   [8, 7, 2]])

matrizfilas = np.sort(dosdim, axis=1, kind='quicksort' )

print("Matriz original:")
print(dosdim)
print("Matriz ordenada por filas: ")
print(matrizfilas)

#Promedio por capa
print("\n*******PROMEDIO POR CAPAS*******")
matriz = [
    [
        [10, 9, 0], #suma = 45    promedio = 45/9 = 5
        [1, 5, 3], 
        [8, 7, 2]
    ],
    [
        [10, 11, 12], #suma = 126    promedio = 126/9 = 14
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21], #suma = 207    promedio = 207/9 = 23
        [22, 23, 24],
        [25, 26, 27]
    ]
]

promedios = []

for capa in matriz:
    suma = 0
    elementos = 0
    for fila in capa:
        for valor in fila:
            suma += valor
            elementos += 1
    promedio = suma / elementos
    promedios.append(promedio)

print("Promedios por capa:", promedios)

