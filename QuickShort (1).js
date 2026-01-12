// Función para intercambiar valores
function intercambiar(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

// Función de partición
function particion(arr, inicio, fin) {
    let pivote = arr[fin]; // Tomamos el último elemento como pivote
    let i = inicio - 1;

    for (let j = inicio; j < fin; j++) {
        if (arr[j] < pivote) {
            i++;
            intercambiar(arr, i, j);
        }
    }

    intercambiar(arr, i + 1, fin);
    return i + 1;
}

// Función QuickSort
function quickSort(arr, inicio, fin) {
    if (inicio < fin) {
        let indicePivote = particion(arr, inicio, fin);

        // Ordenamos recursivamente los elementos a la izquierda y derecha del pivote
        quickSort(arr, inicio, indicePivote - 1);
        quickSort(arr, indicePivote + 1, fin);
    }
}

// Programa principal
function main() {
    let n = parseInt(prompt("¿Cuántos elementos quieres ordenar?"));
    let arreglo = [];

    for (let i = 0; i < n; i++) {
        let num = parseInt(prompt(`Ingresa el elemento ${i + 1}:`));
        arreglo.push(num);
    }

    quickSort(arreglo, 0, n - 1);

    console.log("Arreglo ordenado:", arreglo);
}

// Ejecutar el programa
main();
