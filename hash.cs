using System;
using System.Collections.Generic;

class Program {
    static List<int> HashSort(int[] a) {
        int maxVal = a[0];
        foreach (int x in a)
            if (x > maxVal) maxVal = x;

        int[] table = new int[maxVal + 1];
        foreach (int x in a)
            table[x] = 1;

        List<int> sorted = new List<int>();
        for (int i = 0; i < table.Length; i++)
            if (table[i] == 1)
                sorted.Add(i);

        return sorted;
    }

    static void Main() {
        int[] a = {70, 15, 2, 51, 60};
        Console.WriteLine("Antes de ordenar:");
        Console.WriteLine(string.Join(" ", a));

        var sorted = HashSort(a);

        Console.WriteLine("Después de ordenar:");
        Console.WriteLine(string.Join(" ", sorted));
    }
}
