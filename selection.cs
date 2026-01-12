using System;

class Program {
    static void SelectionSort(int[] a) {
        for (int i = 0; i < a.Length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < a.Length; j++) {
                if (a[j] < a[minIndex])
                    minIndex = j;
            }
            int temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
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
        SelectionSort(a);
        Console.WriteLine("Después de ordenar:");
        PrintArr(a);
    }
}
