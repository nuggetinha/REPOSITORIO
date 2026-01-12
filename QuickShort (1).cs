using System;

class Program
{
    // Función para intercambiar valores
    static void Intercambiar(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    // Función de partición
    static int Particion(int[] arreglo, int inicio, int fin)
    {
        int pivote = arreglo[fin]; // Tomamos el último elemento como pivote
        int i = inicio - 1;

        for (int j = inicio; j < fin; j++)
        {
            if (arreglo[j] < pivote)
            {
                i++;
                Intercambiar(ref arreglo[i], ref arreglo[j]);
            }
        }
        Intercambiar(ref arreglo[i + 1], ref arreglo[fin]);
        return i + 1;
    }

    // Función QuickSort
    static void QuickSort(int[] arreglo, int inicio, int fin)
    {
        if (inicio < fin)
        {
            int indicePivote = Particion(arreglo, inicio, fin);

            // Ordenamos recursivamente los elementos a la izquierda y derecha del pivote
            QuickSort(arreglo, inicio, indicePivote - 1);
            QuickSort(arreglo, indicePivote + 1, fin);
        }
    }

    static void Main()
    {
        Console.Write("¿Cuántos elementos quieres ordenar? ");
        int n = int.Parse(Console.ReadLine());

        int[] arreglo = new int[n];
        Console.WriteLine($"Ingresa los {n} elementos:");

        for (int i = 0; i < n; i++)
        {
            arreglo[i] = int.Parse(Console.ReadLine());
        }

        QuickSort(arreglo, 0, n - 1);

        Console.Write("Arreglo ordenado: ");
        for (int i = 0; i < n; i++)
        {
            Console.Write(arreglo[i] + " ");
        }
        Console.WriteLine();
    }
}

