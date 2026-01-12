using System;

class Program {
    static void BubbleSort(int[] a) {
        for (int i = 0; i < a.Length - 1; i++) {
            for (int j = 0; j < a.Length - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
    }

    static void PrintArr(int[] a) {
        foreach (int x in a)
            Console.Write(x + " ");
        Console.WriteLine();
    }

    static void Main() {
        int[] a = {70, 15, 2, 51, 60};
        Console.WriteLine("Antes de ordenar:");
        PrintArr(a);
        BubbleSort(a);
        Console.WriteLine("Después de ordenar:");
        PrintArr(a);
    }
}
