function getMax(a) {
    return Math.max(...a);
}

function countingSort(a, exp) {
    let n = a.length;
    let output = new Array(n);
    let count = new Array(10).fill(0);

    for (let i = 0; i < n; i++)
        count[Math.floor(a[i] / exp) % 10]++;

    for (let i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (let i = n - 1; i >= 0; i--) {
        let index = Math.floor(a[i] / exp) % 10;
        output[count[index] - 1] = a[i];
        count[index]--;
    }

    for (let i = 0; i < n; i++)
        a[i] = output[i];
}

function radixSort(a) {
    let max = getMax(a);
    for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10)
        countingSort(a, exp);
}

function printArr(a) {
    console.log(a.join(" "));
}

let a = [170, 45, 75, 90, 802, 24, 2, 66];
console.log("Antes de ordenar:");
printArr(a);
radixSort(a);
console.log("Después de ordenar:");
printArr(a);
