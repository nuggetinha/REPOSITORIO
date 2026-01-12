function bubbleSort(a) {
    for (let i = 0; i < a.length - 1; i++) {
        for (let j = 0; j < a.length - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                let temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}

function printArr(a) {
    console.log(a.join(" "));
}

let a = [70, 15, 2, 51, 60];
console.log("Antes de ordenar:");
printArr(a);
bubbleSort(a);
console.log("Después de ordenar:");
printArr(a);
