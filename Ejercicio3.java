import java.util.ArrayList;

public class Ejercicio3 {
    public static void main(String[] args) {
        ArrayList<Integer> arrayNumeros = new ArrayList<>();
        for (int i = 1; i <= 10; i++) arrayNumeros.add(i);

        System.out.println("Recorrido inicial:");
        for (int i = 0; i < arrayNumeros.size(); i++) {
            System.out.println("[" + i + "]: " + arrayNumeros.get(i));
        }

        System.out.println("Buscando el valor 8:");
        for (int i = 0; i < arrayNumeros.size(); i++) {
            if (arrayNumeros.get(i) == 8) {
                System.out.println("¡Encontrado! El valor 8 está en la posición " + i);
                break;
            }
        }

        arrayNumeros.add(5, 22);

        System.out.println("Recorrido después de la inserción:");
        for (int i = 0; i < arrayNumeros.size(); i++) {
            System.out.println("[" + i + "]: " + arrayNumeros.get(i));
        }

        System.out.println("Recorrido inverso:");
        for (int i = arrayNumeros.size() - 1; i >= 0; i--) {
            System.out.println("[" + i + "]: " + arrayNumeros.get(i));
        }
    }
}
