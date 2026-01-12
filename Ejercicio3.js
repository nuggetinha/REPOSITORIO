let arrayNumeros = [1,2,3,4,5,6,7,8,9,10];

console.log("Recorrido inicial:");
arrayNumeros.forEach((num, i) => console.log(`[${i}]: ${num}`));

console.log("Buscando el valor 8:");
for (let i = 0; i < arrayNumeros.length; i++) {
    if (arrayNumeros[i] === 8) {
        console.log(`¡Encontrado! El valor 8 está en la posición ${i}`);
        break;
    }
}

arrayNumeros.splice(5, 0, 22);

console.log("Recorrido después de la inserción:");
arrayNumeros.forEach((num, i) => console.log(`[${i}]: ${num}`));

console.log("Recorrido inverso:");
for (let i = arrayNumeros.length - 1; i >= 0; i--) {
    console.log(`[${i}]: ${arrayNumeros[i]}`);
}
