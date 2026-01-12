def bucket_sort(a):
    n = len(a)
    buckets = [[] for _ in range(n)]

    for num in a:
        index = int(num * n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

a = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Antes de ordenar:", a)
sorted_a = bucket_sort(a)
print("Después de ordenar:", sorted_a)
