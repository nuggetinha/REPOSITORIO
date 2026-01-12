class Nodo {
    int dato;
    Nodo sig;

    Nodo(int v) {
        dato = v;
        sig = null;
    }
}

public class Lista {
    Nodo inicio;

    public Lista() {
        inicio = null;
    }

    public void insertarInicio(int v) {
        Nodo nuevo = new Nodo(v);
        nuevo.sig = inicio;
        inicio = nuevo;
    }

    public void insertarFinal(int v) {
        Nodo nuevo = new Nodo(v);
        if (inicio == null) {
            inicio = nuevo;
            return;
        }
        Nodo aux = inicio;
        while (aux.sig != null) aux = aux.sig;
        aux.sig = nuevo;
    }

    public boolean buscar(int v) {
        Nodo aux = inicio;
        while (aux != null) {
            if (aux.dato == v) return true;
            aux = aux.sig;
        }
        return false;
    }

    public void eliminar(int v) {
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

    public void mostrar() {
        Nodo aux = inicio;
        while (aux != null) {
            System.out.print(aux.dato + " -> ");
            aux = aux.sig;
        }
        System.out.println("NULL");
    }

    public static void main(String[] args) {
        Lista l = new Lista();
        l.insertarInicio(10);
        l.insertarFinal(20);
        l.insertarFinal(30);
        l.mostrar();
    }
}
