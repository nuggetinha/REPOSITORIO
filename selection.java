public class Main {
    public static void selectionSort(int[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIndex])
                    minIndex = j;
            }
            int temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
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
        selectionSort(a);
        System.out.println("Después de ordenar:");
        printArr(a);
    }
}
