def hash_sort(a):
    max_val = max(a)
    table = [0] * (max_val + 1)

    for num in a:
        table[num] = 1

    sorted_a = []
    for i in range(len(table)):
        if table[i] == 1:
            sorted_a.append(i)

    return sorted_a

a = [70, 15, 2, 51, 60]
print("Antes de ordenar:", a)
a = hash_sort(a)
print("Después de ordenar:", a)
