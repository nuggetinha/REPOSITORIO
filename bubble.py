def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

a = [70, 15, 2, 51, 60]
print("Antes de ordenar:", a)
bubble_sort(a)
print("Después de ordenar:", a)
