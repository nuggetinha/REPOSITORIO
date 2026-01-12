class Cola {
    constructor(size) {
        this.frente = -1;
        this.atras = -1;
        this.tam = size;
        this.arr = new Array(size);
    }

    estaVacia() {
        return this.frente === -1;
    }

    estaLlena() {
        return this.atras === this.tam - 1;
    }

    enqueue(valor) {
        if (this.estaLlena()) {
            console.log("Cola llena");
            return;
        }
        if (this.frente === -1) this.frente = 0;
        this.arr[++this.atras] = valor;
    }

    dequeue() {
        if (this.estaVacia()) {
            console.log("Cola vacía");
            return -1;
        }
        const x = this.arr[this.frente];
        if (this.frente === this.atras) this.frente = this.atras = -1;
        else this.frente++;
        return x;
    }

    peek() {
        if (this.estaVacia()) return -1;
        return this.arr[this.frente];
    }
}

// Ejemplo
let q = new Cola(5);
q.enqueue(10);
q.enqueue(20);
console.log("Frente:", q.peek());
console.log("Dequeue:", q.dequeue());
