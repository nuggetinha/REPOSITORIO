class Nodo {
    constructor(v) {
        this.dato = v;
        this.sig = null;
    }
}

class Lista {
    constructor() {
        this.inicio = null;
    }

    insertarInicio(v) {
        let nuevo = new Nodo(v);
        nuevo.sig = this.inicio;
        this.inicio = nuevo;
    }

    insertarFinal(v) {
        let nuevo = new Nodo(v);
        if (!this.inicio) {
            this.inicio = nuevo;
            return;
        }
        let aux = this.inicio;
        while (aux.sig) aux = aux.sig;
        aux.sig = nuevo;
    }

    buscar(v) {
        let aux = this.inicio;
        while (aux) {
            if (aux.dato === v) return true;
            aux = aux.sig;
        }
        return false;
    }

    eliminar(v) {
        if (!this.inicio) return;

        if (this.inicio.dato === v) {
            this.inicio = this.inicio.sig;
            return;
        }

        let aux = this.inicio;
        while (aux.sig && aux.sig.dato !== v)
            aux = aux.sig;

        if (aux.sig)
            aux.sig = aux.sig.sig;
    }

    mostrar() {
        let aux = this.inicio;
        let out = "";
        while (aux) {
            out += aux.dato + " -> ";
            aux = aux.sig;
        }
        console.log(out + "NULL");
    }
}

// Ejemplo
let l = new Lista();
l.insertarInicio(10);
l.insertarFinal(20);
l.insertarFinal(30);
l.mostrar();
