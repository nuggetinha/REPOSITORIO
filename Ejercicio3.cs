using system;
using System.Collections.Generic;

List<int> arrayNumeros = new List<int>();
for (int i = 1; i <= 10; i++) arrayNumeros.Add(i);

Console.WriteLine("Recorrido inicial:");
for (int i = 0; i < arrayNumeros.Count; i++) {
    Console.WriteLine("[" + i + "]: " + arrayNumeros[i]);
}

Console.WriteLine("Buscando el valor 8:");
for (int i = 0; i < arrayNumeros.Count; i++) {
    if (arrayNumeros[i] == 8) {
        Console.WriteLine("¡Encontrado! El valor 8 está en la posición " + i);
        break;
    }
}

arrayNumeros.Insert(5, 22);

Console.WriteLine("Recorrido después de la inserción:");
for (int i = 0; i < arrayNumeros.Count; i++) {
    Console.WriteLine("[" + i + "]: " + arrayNumeros[i]);
}

Console.WriteLine("Recorrido inverso:");
for (int i = arrayNumeros.Count - 1; i >= 0; i--) {
    Console.WriteLine("[" + i + "]: " + arrayNumeros[i]);
}
