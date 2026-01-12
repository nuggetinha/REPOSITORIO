function bucketSort(a) {
    let n = a.length;
    let buckets = Array.from({ length: n }, () => []);

    for (let i = 0; i < n; i++) {
        let index = Math.floor(a[i] * n);
        buckets[index].push(a[i]);
    }

    for (let i = 0; i < n; i++)
        buckets[i].sort((x, y) => x - y);

    return buckets.flat();
}

let a = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68];
console.log("Antes de ordenar:");
console.log(a.join(" "));
a = bucketSort(a);
console.log("Después de ordenar:");
console.log(a.join(" "));
