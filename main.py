#Eliminar duplicados
unadim = [1, 2, 2, 3, 4, 4, 5]
sinduplicados = list(set(unadim))
print(sinduplicados)

#Ordenar por filas
import numpy as np
dosdim = np.array([[10, 9, 0],
                   [1, 5, 3],
                   [8, 7, 2]])

matrizfilas = np.sort(dosdim, axis=1, kind='quicksort' )

print("Matriz original:")
print(dosdim)
print("\nMatriz ordenada por filas: ")
print(matrizfilas)

#Promedio por capa
matriz = [
    [
        [10, 9, 0],
        [1, 5, 3],
        [8, 7, 2]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
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

print("\nPromedios por capa:", promedios)

