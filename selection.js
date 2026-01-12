function selectionSort(a) {
    for (let i = 0; i < a.length - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < a.length; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        }
        let temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
}

function printArr(a) {
    console.log(a.join(" "));
}

let a = [70, 15, 2, 51, 60];
console.log("Antes de ordenar:");
printArr(a);
selectionSort(a);
console.log("Después de ordenar:");
printArr(a);
