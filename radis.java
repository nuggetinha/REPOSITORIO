public class Main {
    static int getMax(int[] a) {
        int max = a[0];
        for (int i = 1; i < a.length; i++)
            if (a[i] > max)
                max = a[i];
        return max;
    }

    static void countingSort(int[] a, int exp) {
        int n = a.length;
        int[] output = new int[n];
        int[] count = new int[10];

        for (int i = 0; i < n; i++)
            count[(a[i] / exp) % 10]++;

        for (int i = 1; i < 10; i++)
            count[i] += count[i - 1];

        for (int i = n - 1; i >= 0; i--) {
            int index = (a[i] / exp) % 10;
            output[count[index] - 1] = a[i];
            count[index]--;
        }

        for (int i = 0; i < n; i++)
            a[i] = output[i];
    }

    static void radixSort(int[] a) {
        int max = getMax(a);
        for (int exp = 1; max / exp > 0; exp *= 10)
            countingSort(a, exp);
    }

    static void printArr(int[] a) {
        for (int x : a)
            System.out.print(x + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int[] a = {170, 45, 75, 90, 802, 24, 2, 66};
        System.out.println("Antes de ordenar:");
        printArr(a);
        radixSort(a);
        System.out.println("Después de ordenar:");
        printArr(a);
    }
}
