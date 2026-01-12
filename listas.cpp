#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* sig;
    Nodo(int v) { dato = v; sig = NULL; }
};

class Lista {
private:
    Nodo* inicio;

public:
    Lista() { inicio = NULL; }

    void insertarInicio(int v) {
        Nodo* nuevo = new Nodo(v);
        nuevo->sig = inicio;
        inicio = nuevo;
    }

    void insertarFinal(int v) {
        Nodo* nuevo = new Nodo(v);
        if (!inicio) { inicio = nuevo; return; }

        Nodo* aux = inicio;
        while (aux->sig) aux = aux->sig;
        aux->sig = nuevo;
    }

    bool buscar(int v) {
        Nodo* aux = inicio;
        while (aux) {
            if (aux->dato == v) return true;
            aux = aux->sig;
        }
        return false;
    }

    void eliminar(int v) {
        if (!inicio) return;

        if (inicio->dato == v) {
            Nodo* tmp = inicio;
            inicio = inicio->sig;
            delete tmp;
            return;
        }

        Nodo* aux = inicio;
        while (aux->sig && aux->sig->dato != v) aux = aux->sig;

        if (aux->sig) {
            Nodo* tmp = aux->sig;
            aux->sig = tmp->sig;
            delete tmp;
        }
    }

    void mostrar() {
        Nodo* aux = inicio;
        while (aux) {
            cout << aux->dato << " -> ";
            aux = aux->sig;
        }
        cout << "NULL\n";
    }
};

int main() {
    Lista l;
    l.insertarInicio(10);
    l.insertarFinal(20);
    l.insertarFinal(30);
    l.mostrar();
}
