using System;

class Program {
    static int GetMax(int[] a) {
        int max = a[0];
        for (int i = 1; i < a.Length; i++)
            if (a[i] > max)
                max = a[i];
        return max;
    }

    static void CountingSort(int[] a, int exp) {
        int n = a.Length;
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

    static void RadixSort(int[] a) {
        int max = GetMax(a);
        for (int exp = 1; max / exp > 0; exp *= 10)
            CountingSort(a, exp);
    }

    static void PrintArr(int[] a) {
        foreach (int x in a)
            Console.Write(x + " ");
        Console.WriteLine();
    }

    static void Main() {
        int[] a = {170, 45, 75, 90, 802, 24, 2, 66};
        Console.WriteLine("Antes de ordenar:");
        PrintArr(a);
        RadixSort(a);
        Console.WriteLine("Después de ordenar:");
        PrintArr(a);
    }
}
