function merge(left, right) {
    let result = [];
    let i = 0, j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }
    }

    return result.concat(left.slice(i)).concat(right.slice(j));
}

function mergeSort(a) {
    if (a.length <= 1) return a;

    let mid = Math.floor(a.length / 2);
    let left = a.slice(0, mid);
    let right = a.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
}

let a = [70, 15, 2, 51, 60];
console.log("Antes de ordenar:", a.join(" "));
a = mergeSort(a);
console.log("Después de ordenar:", a.join(" "));
