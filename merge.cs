using System;

class Program {
    static void Merge(int[] a, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = a[left + i];
        for (int j = 0; j < n2; j++)
            R[j] = a[mid + 1 + j];

        int k = left, i1 = 0, j1 = 0;

        while (i1 < n1 && j1 < n2) {
            if (L[i1] <= R[j1])
                a[k++] = L[i1++];
            else
                a[k++] = R[j1++];
        }

        while (i1 < n1)
            a[k++] = L[i1++];
        while (j1 < n2)
            a[k++] = R[j1++];
    }

    static void MergeSort(int[] a, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            MergeSort(a, left, mid);
            MergeSort(a, mid + 1, right);
            Merge(a, left, mid, right);
        }
    }

    static void Main() {
        int[] a = {70, 15, 2, 51, 60};
        Console.WriteLine("Antes de ordenar:");
        Console.WriteLine(string.Join(" ", a));
        MergeSort(a, 0, a.Length - 1);
        Console.WriteLine("Después de ordenar:");
        Console.WriteLine(string.Join(" ", a));
    }
}
