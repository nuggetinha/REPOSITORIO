public class Main {
    public static void insertionSort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int temp = a[i];
            int j = i - 1;
            while (j >= 0 && temp < a[j]) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = temp;
        }
    }

    public static void printArr(int[] a) {
        for (int x : a)
            System.out.print(x + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int[] a = {70, 15, 2, 51, 60};
        System.out.println("Antes de ordenar los elementos del arreglo:");
        printArr(a);
        insertionSort(a);
        System.out.println("Después de ordenar los elementos del arreglo:");
        printArr(a);
    }
}