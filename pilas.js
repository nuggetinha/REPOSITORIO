const MAX_SIZE = 100; // Tamaño máximo de la pila
let stack = new Array(MAX_SIZE); // Arreglo para almacenar los elementos de la pila
let top = -1; // Índice del elemento superior de la pila

// Función para agregar un elemento a la pila
function push(item) {
    if (top === MAX_SIZE - 1) { // Verifica si la pila está llena
        console.log("Stack Overflow"); // Mensaje de error
        return; // Sale de la función
    }
    stack[++top] = item; // Incrementa el índice y agrega el elemento
}

// Función para eliminar y retornar el elemento superior de la pila
function pop() {
    if (top === -1) { // Verifica si la pila está vacía
        console.log("Stack Underflow"); // Mensaje de error
        return -1; // Retorna -1 para indicar que la pila está vacía
    }
    return stack[top--]; // Retorna el elemento superior y decrementa el índice
}

// Función para ver el elemento superior sin eliminarlo
function peek() {
    if (top === -1) { // Verifica si la pila está vacía
        console.log("Pila vacía"); // Mensaje de error
        return -1; // Retorna -1 para indicar que la pila está vacía
    }
    return stack[top]; // Retorna el elemento superior sin modificar el índice
}

// Función para verificar si la pila está vacía
function isEmpty() {
    return top === -1; // Retorna true si está vacía, false en caso contrario
}

// Función para verificar si la pila está llena
function isFull() {
    return top === MAX_SIZE - 1; // Retorna true si está llena, false en caso contrario
}

// Ejemplo de uso de la pila
push(10); // Agrega elementos a la pila
push(20); // agrega otro elemento
push(30); // agrega otro elemento

console.log("Elemento Superior: " + peek()); // Muestra el elemento superior
console.log("Extrae elemento: " + pop()); // Elimina y muestra el elemento superior
cons