using System;

class Program {
    static void Heapify(int[] a, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && a[left] > a[largest])
            largest = left;

        if (right < n && a[right] > a[largest])
            largest = right;

        if (largest != i) {
            (a[i], a[largest]) = (a[largest], a[i]);
            Heapify(a, n, largest);
        }
    }

    static void HeapSort(int[] a) {
        int n = a.Length;

        for (int i = n / 2 - 1; i >= 0; i--)
            Heapify(a, n, i);

        for (int i = n - 1; i > 0; i--) {
            (a[0], a[i]) = (a[i], a[0]);
            Heapify(a, i, 0);
        }
    }

    static void Main() {
        int[] a = {70, 15, 2, 51, 60};
        Console.WriteLine("Antes de ordenar:");
        Console.WriteLine(string.Join(" ", a));
        HeapSort(a);
        Console.WriteLine("Después de ordenar:");
        Console.WriteLine(string.Join(" ", a));
    }
}
