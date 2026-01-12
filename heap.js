function heapify(a, n, i) {
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

    if (left < n && a[left] > a[largest]) largest = left;
    if (right < n && a[right] > a[largest]) largest = right;

    if (largest !== i) {
        [a[i], a[largest]] = [a[largest], a[i]];
        heapify(a, n, largest);
    }
}

function heapSort(a) {
    let n = a.length;

    for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
        heapify(a, n, i);

    for (let i = n - 1; i > 0; i--) {
        [a[0], a[i]] = [a[i], a[0]];
        heapify(a, i, 0);
    }
}

let a = [70, 15, 2, 51, 60];
console.log("Antes de ordenar:", a.join(" "));
heapSort(a);
console.log("Después de ordenar:", a.join(" "));
