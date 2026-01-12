import java.util.Scanner;

public class QuickSortJava {

    // Función para intercambiar valores
    public static void intercambiar(int[] arreglo, int i, int j) {
        int temp = arreglo[i];
        arreglo[i] = arreglo[j];
        arreglo[j] = temp;
    }

    // Función de partición
    public static int particion(int[] arreglo, int inicio, int fin) {
        int pivote = arreglo[fin];  // Tomamos el último elemento como pivote
        int i = inicio - 1;

        for (int j = inicio; j < fin; j++) {
            if (arreglo[j] < pivote) {
                i++;
                intercambiar(arreglo, i, j);
            }
        }

        intercambiar(arreglo, i + 1, fin);
        return i + 1;
    }

    // Función QuickSort
    public static void quickSort(int[] arreglo, int inicio, int fin) {
        if (inicio < fin) {
            int indicePivote = particion(arreglo, inicio, fin);

            // Ordenamos recursivamente los elementos a la izquierda y derecha del pivote
            quickSort(arreglo, inicio, indicePivote - 1);
            quickSort(arreglo, indicePivote + 1, fin);
        }
    }

    // Programa principal
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Cuantos elementos quieres ordenar? ");
        int n = sc.nextInt();
        int[] arreglo = new int[n];

        System.out.println("Ingresa los " + n + " elementos:");
        for (int i = 0; i < n; i++) {
            arreglo[i] = sc.nextInt();
        }

        quickSort(arreglo, 0, n - 1);

        System.out.print("Arreglo ordenado: ");
        for (int num : arreglo) {
            System.out.print(num + " ");
        }
    }
}