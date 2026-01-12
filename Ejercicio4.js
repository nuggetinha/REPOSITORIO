let matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
];

console.log("Matriz");
matriz.forEach(fila => console.log(fila));

console.log("Horizontal");
for (let i = 0; i < matriz.length; i++) {
    for (let j = 0; j < matriz[i].length; j++) {
        console.log(`[${i}][${j}]: ${matriz[i][j]}`);
    }
}

console.log("Vertical");
for (let j = 0; j < matriz[0].length; j++) {
    for (let i = 0; i < matriz.length; i++) {
        console.log(`[${i}][${j}]: ${matriz[i][j]}`);
    }
}
