function hashSort(a) {
    let max = Math.max(...a);
    let table = new Array(max + 1).fill(0);

    for (let num of a)
        table[num] = 1;

    let sorted = [];
    for (let i = 0; i < table.length; i++)
        if (table[i] === 1)
            sorted.push(i);

    return sorted;
}

let a = [70, 15, 2, 51, 60];
console.log("Antes de ordenar:");
console.log(a.join(" "));
let sorted = hashSort(a);
console.log("Después de ordenar:");
console.log(sorted.join(" "));
