using System;

int[,] matriz = {
    {10, 20, 30},
    {40, 50, 60},
    {70, 80, 90}
};

Console.WriteLine("Matriz");
for (int i = 0; i < matriz.GetLength(0); i++)
{
    for (int j = 0; j < matriz.GetLength(1); j++)
    {
        Console.Write(matriz[i, j] + " ");
    }
    Console.WriteLine();
}

Console.WriteLine("Horizontal");
for (int i = 0; i < matriz.GetLength(0); i++)
{
    for (int j = 0; j < matriz.GetLength(1); j++)
    {
        Console.WriteLine($"[{i}][{j}]: {matriz[i, j]}");
    }
}

Console.WriteLine("Vertical");
for (int j = 0; j < matriz.GetLength(1); j++) {
    for (int i = 0; i < matriz.GetLength(0); i++) {
        Console.WriteLine($"[{i}][{j}]: {matriz[i, j]}");
    }
}