def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

a = [70, 15, 2, 51, 60]
print("Antes de ordenar:", a)
selection_sort(a)
print("Después de ordenar:", a)
