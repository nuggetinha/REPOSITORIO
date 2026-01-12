class Alumno {
    String nombre;
    String calificacion;

    Alumno(String nombre, String calificacion) {
        this.nombre = nombre;
        this.calificacion = calificacion;
    }

    @Override
    public String toString() {
        return nombre + " " + calificacion;
    }
}

public class Ejercicio2 {
    public static void main(String[] args) {
        Alumno[] alumnos = {
            new Alumno("Pedro", "20"),
            new Alumno("Alejandro", "22"),
            new Alumno("Carlos", "18")
        };

        System.out.println("Alumnos + Calificación:");
        for (int i = 0; i < alumnos.length; i++) {
            System.out.println("[" + i + "]: " + alumnos[i]);
        }
    }
}
