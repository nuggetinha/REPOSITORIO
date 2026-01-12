import java.util.*;

public class Main {
    static List<Integer> hashSort(int[] a) {
        int max = Arrays.stream(a).max().getAsInt();
        int[] table = new int[max + 1];

        for (int x : a)
            table[x] = 1;

        List<Integer> sorted = new ArrayList<>();
        for (int i = 0; i < table.length; i++)
            if (table[i] == 1)
                sorted.add(i);

        return sorted;
    }

    public static void main(String[] args) {
        int[] a = {70, 15, 2, 51, 60};
        System.out.println("Antes de ordenar:");
        System.out.println(Arrays.toString(a));

        List<Integer> sorted = hashSort(a);

        System.out.println("Después de ordenar:");
        System.out.println(sorted);
    }
}
