matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Matriz")
for i in matriz:
    print(i)

print("Horizontal")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"[{i}][{j}]: {matriz[i][j]}")

print("Vertical")
for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(f"[{i}][{j}]: {matriz[i][j]}")
