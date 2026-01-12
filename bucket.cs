using System;
using System.Collections.Generic;

class Program {
    static void BucketSort(float[] a) {
        int n = a.Length;
        List<float>[] buckets = new List<float>[n];

        for (int i = 0; i < n; i++)
            buckets[i] = new List<float>();

        for (int i = 0; i < n; i++) {
            int index = (int)(a[i] * n);
            buckets[index].Add(a[i]);
        }

        for (int i = 0; i < n; i++)
            buckets[i].Sort();

        int k = 0;
        for (int i = 0; i < n; i++)
            foreach (float val in buckets[i])
                a[k++] = val;
    }

    static void PrintArr(float[] a) {
        foreach (float x in a)
            Console.Write(x + " ");
        Console.WriteLine();
    }

    static void Main() {
        float[] a = {0.78f, 0.17f, 0.39f, 0.26f, 0.72f, 0.94f, 0.21f, 0.12f, 0.23f, 0.68f};
        Console.WriteLine("Antes de ordenar:");
        PrintArr(a);
        BucketSort(a);
        Console.WriteLine("Después de ordenar:");
        PrintArr(a);
    }
}
