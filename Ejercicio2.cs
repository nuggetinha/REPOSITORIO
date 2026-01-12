using system;
using system.Collections.Generic;

class Alumno
{
    public string Nombre { get; set; }
    public string Calificacion { get; set; }

    public Alumno(string nombre, string calificacion)
    {
        Nombre = nombre;
        calificacion = Calificacion;
    } 

    public override string ToString() {
        return Nombre + " " + Calificacion;
    }
}

List<Alumno> alumnos = new List<Alumno> {
    new Alumno("Pedro", "20"),
    new Alumno("Alejandro", "22"),
    new Alumno("Carlos", "18")
};

Console.WriteLine("Alumnos + Calificación:");
for (int i = 0; i < alumnos.Count; i++) {
    Console.WriteLine("[" + i + "]: " + alumnos[i]);
}