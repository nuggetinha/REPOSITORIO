#Recorrido en Python
arr = [40,50,60,70,80,90]
print("recorrido lineal (Secuencial):", end=" ")
print("\nLos elementos del array son:", end=" ")
for idx in arr:
    print(idx, end=" ")
print()

#Recorrido Inverso en Python
ar=[40,50,60,70,80,90]
print("Recorrido inverso del array: ", end=" ")
print("\nLos elemntos del array son: ", end=" ")
for idx in range(len(ar)-1,-1,-1):
    print(ar[idx], end=" ")
print()

