class Alumno {
    constructor(nombre, calificacion) {
        this.nombre = nombre;
        this.calificacion = calificacion;
    }

    toString() {
        return `${this.nombre} ${this.calificacion}`;
    }
}

let alumnos = [
    new Alumno("Pedro", "20"),
    new Alumno("Alejandro", "22"),
    new Alumno("Carlos", "18")
];

console.log("Alumnos + Calificación:");
alumnos.forEach((persona, i) => {
    console.log(`[${i}]: ${persona.toString()}`);
});