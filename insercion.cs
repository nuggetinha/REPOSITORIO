using System;

class Program {
    static void InsertionSort(int[] a) {
        for (int i = 1; i < a.Length; i++) {
            int temp = a[i];
            int j = i - 1;
            while (j >= 0 && temp < a[j]) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = temp;
        }
    }

    static void PrintArr(int[] a) {
        foreach (int x in a)
            Console.Write(x + " ");
        Console.WriteLine();
    }

    static void Main() {
        int[] a = {70, 15, 2, 51, 60};
        Console.WriteLine("Antes de ordenar los elementos del arreglo:");
        PrintArr(a);
        InsertionSort(a);
        Console.WriteLine("Después de ordenar los elementos del arreglo:");
        PrintArr(a);
    }
}