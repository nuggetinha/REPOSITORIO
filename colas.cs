using System;

class Cola {
    int frente, atras, tam;
    int[] arr;

    public Cola(int size) {
        frente = -1;
        atras = -1;
        tam = size;
        arr = new int[tam];
    }

    public bool EstaVacia() {
        return frente == -1;
    }

    public bool EstaLlena() {
        return atras == tam - 1;
    }

    public void Enqueue(int valor) {
        if (EstaLlena()) {
            Console.WriteLine("Cola llena");
            return;
        }
        if (frente == -1) frente = 0;
        arr[++atras] = valor;
    }

    public int Dequeue() {
        if (EstaVacia()) {
            Console.WriteLine("Cola vacía");
            return -1;
        }
        int x = arr[frente];
        if (frente == atras) frente = atras = -1;
        else frente++;
        return x;
    }

    public int Peek() {
        if (EstaVacia()) return -1;
        return arr[frente];
    }
}

class Program {
    static void Main() {
        Cola q = new Cola(5);
        q.Enqueue(10);
        q.Enqueue(20);
        q.Enqueue(30);

        Console.WriteLine("Frente: " + q.Peek());
        Console.WriteLine("Dequeue: " + q.Dequeue());
    }
}
