import java.util.*;

public class Main {
    public static void bucketSort(float[] a) {
        int n = a.length;
        ArrayList<Float>[] buckets = new ArrayList[n];

        for (int i = 0; i < n; i++)
            buckets[i] = new ArrayList<>();

        for (float num : a) {
            int index = (int)(num * n);
            buckets[index].add(num);
        }

        for (int i = 0; i < n; i++)
            Collections.sort(buckets[i]);

        int k = 0;
        for (int i = 0; i < n; i++)
            for (float val : buckets[i])
                a[k++] = val;
    }

    public static void printArr(float[] a) {
        for (float x : a)
            System.out.print(x + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        float[] a = {0.78f, 0.17f, 0.39f, 0.26f, 0.72f, 0.94f, 0.21f, 0.12f, 0.23f, 0.68f};
        System.out.println("Antes de ordenar:");
        printArr(a);
        bucketSort(a);
        System.out.println("Después de ordenar:");
        printArr(a);
    }
}
