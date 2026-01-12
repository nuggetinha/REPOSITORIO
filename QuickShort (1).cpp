#include <iostream>
using namespace std;

// Función para intercambiar valores
void intercambiar(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Función de partición
int particion(int arreglo[], int inicio, int fin) {
    int pivote = arreglo[fin]; // Tomamos el último elemento como pivote
    int i = inicio - 1;

    for (int j = inicio; j < fin; j++) {
        if (arreglo[j] < pivote) {
            i++;
            intercambiar(arreglo[i], arreglo[j]);
        }
    }
    intercambiar(arreglo[i + 1], arreglo[fin]);
    return i + 1;
}

// Función QuickSort
void quickSort(int arreglo[], int inicio, int fin) {
    if (inicio < fin) {
        int indicePivote = particion(arreglo, inicio, fin);

        // Ordenamos recursivamente los elementos a la izquierda y derecha del pivote
        quickSort(arreglo, inicio, indicePivote - 1);
        quickSort(arreglo, indicePivote + 1, fin);
    }
}

int main() {
    int n;
    cout << "Cuantos elementos quieres ordenar? ";
    cin >> n;

    int arreglo[n];
    cout << "Ingresa los " << n << " elementos:\n";
    for (int i = 0; i < n; i++) {
        cin >> arreglo[i];
    }

    quickSort(arreglo, 0, n - 1);

    cout << "Arreglo ordenado: ";
    for (int i = 0; i < n; i++) {
        cout << arreglo[i] << " ";
    }
    cout << endl;

    return 0;
}
