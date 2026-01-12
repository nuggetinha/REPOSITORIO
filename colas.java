public class Cola {
    int frente, atras, tam;
    int[] arr;

    public Cola(int size) {
        frente = -1;
        atras = -1;
        tam = size;
        arr = new int[tam];
    }

    public boolean estaVacia() {
        return frente == -1;
    }

    public boolean estaLlena() {
        return atras == tam - 1;
    }

    public void enqueue(int valor) {
        if (estaLlena()) {
            System.out.println("Cola llena");
            return;
        }
        if (frente == -1) frente = 0;
        arr[++atras] = valor;
    }

    public int dequeue() {
        if (estaVacia()) {
            System.out.println("Cola vacía");
            return -1;
        }
        int x = arr[frente];
        if (frente == atras) frente = atras = -1;
        else frente++;
        return x;
    }

    public int peek() {
        if (estaVacia()) return -1;
        return arr[frente];
    }

    public static void main(String[] args) {
        Cola q = new Cola(5);
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);

        System.out.println("Frente: " + q.peek());
        System.out.println("Dequeue: " + q.dequeue());
    }
}
