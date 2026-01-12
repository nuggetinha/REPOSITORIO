#include <iostream>
using namespace std;

class Cola {
private:
    int frente, atras, tam;
    int* arr;

public:
    Cola(int size) {
        tam = size;
        arr = new int[tam];
        frente = -1;
        atras = -1;
    }

    ~Cola() {
        delete[] arr;
    }

    bool estaVacia() {
        return frente == -1;
    }

    bool estaLlena() {
        return atras == tam - 1;
    }

    void enqueue(int valor) {
        if (estaLlena()) {
            cout << "Cola llena\n";
            return;
        }
        if (frente == -1) frente = 0;
        arr[++atras] = valor;
    }

    int dequeue() {
        if (estaVacia()) {
            cout << "Cola vacía\n";
            return -1;
        }
        int x = arr[frente];
        if (frente == atras) {
            frente = atras = -1;
        } else {
            frente++;
        }
        return x;
    }

    int peek() {
        if (estaVacia()) return -1;
        return arr[frente];
    }
};

int main() {
    Cola q(5);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Frente: " << q.peek() << endl;
    cout << "Dequeue: " << q.dequeue() << endl;
    cout << "Dequeue: " << q.dequeue() << endl;

    return 0;
}
