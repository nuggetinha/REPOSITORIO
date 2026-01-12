using System;

class Program {
    static int Partition(int[] a, int low, int high) {
        int pivot = a[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (a[j] <= pivot) {
                i++;
                (a[i], a[j]) = (a[j], a[i]);
            }
        }
        (a[i + 1], a[high]) = (a[high], a[i + 1]);
        return i + 1;
    }

    static void QuickSort(int[] a, int low, int high) {
        if (low < high) {
            int pi = Partition(a, low, high);
            QuickSort(a, low, pi - 1);
            QuickSort(a, pi + 1, high);
        }
    }

    static void Main() {
        int[] a = {70, 15, 2, 51, 60};
        Console.WriteLine("Antes de ordenar:");
        Console.WriteLine(string.Join(" ", a));
        QuickSort(a, 0, a.Length - 1);
        Console.WriteLine("Después de ordenar:");
        Console.WriteLine(string.Join(" ", a));
    }
}
