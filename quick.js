function partition(a, low, high) {
    let pivot = a[high];
    let i = low - 1;

    for (let j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            [a[i], a[j]] = [a[j], a[i]];
        }
    }

    [a[i + 1], a[high]] = [a[high], a[i + 1]];
    return i + 1;
}

function quickSort(a, low, high) {
    if (low < high) {
        let pi = partition(a, low, high);
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}

let a = [70, 15, 2, 51, 60];
console.log("Antes de ordenar:", a.join(" "));
quickSort(a, 0, a.length - 1);
console.log("Después de ordenar:", a.join(" "));
