using System;

class Nodo {
    public int dato;
    public Nodo sig;

    public Nodo(int v) {
        dato = v;
        sig = null;
    }
}

class Lista {
    Nodo inicio;

    public Lista() {
        inicio = null;
    }

    public void InsertarInicio(int v) {
        Nodo nuevo = new Nodo(v);
        nuevo.sig = inicio;
        inicio = nuevo;
    }

    public void InsertarFinal(int v) {
        Nodo nuevo = new Nodo(v);
        if (inicio == null) {
            inicio = nuevo;
            return;
        }
        Nodo aux = inicio;
        while (aux.sig != null) aux = aux.sig;
        aux.sig = nuevo;
    }

    public bool Buscar(int v) {
        Nodo aux = inicio;
        while (aux != null) {
            if (aux.dato == v) return true;
            aux = aux.sig;
        }
        return false;
    }

    public void Eliminar(int v) {
        if (inicio == null) return;

        if (inicio.dato == v) {
            inicio = inicio.sig;
            return;
        }

        Nodo aux = inicio;
        while (aux.sig != null && aux.sig.dato != v)
            aux = aux.sig;

        if (aux.sig != null)
            aux.sig = aux.sig.sig;
    }

    public void Mostrar() {
        Nodo aux = inicio;
        while (aux != null) {
            Console.Write(aux.dato + " -> ");
            aux = aux.sig;
        }
        Console.WriteLine("NULL");
    }
}

class Program {
    static void Main() {
        Lista l = new Lista();
        l.InsertarInicio(10);
        l.InsertarFinal(20);
        l.InsertarFinal(30);
        l.Mostrar();
    }
}
