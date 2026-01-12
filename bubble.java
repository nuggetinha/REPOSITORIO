public class Main {
    public static void bubbleSort(int[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            for (int j = 0; j < a.length - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
    }

    public static void printArr(int[] a) {
        for (int x : a)
            System.out.print(x + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int[] a = {70, 15, 2, 51, 60};
        System.out.println("Antes de ordenar:");
        printArr(a);
        bubbleSort(a);
        System.out.println("Después de ordenar:");
        printArr(a);
    }
}
