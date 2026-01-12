class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def __str__(self):
        return f"{self.nombre} {self.calificacion}"

alumnos = [
    Alumno("Pedro", "20"),
    Alumno("Alejandro", "22"),
    Alumno("Carlos", "18")
]

print("Alumnos + Calificación:")
for i, persona in enumerate(alumnos):
    print(f"[{i}]: {persona}")