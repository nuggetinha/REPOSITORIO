#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Alumno {
    string nombre;
    string calificacion;

    string toString() const {
        return nombre + " " + calificacion;
    }
};

int main() {
    vector<Alumno> alumnos = {
        {"Pedro", "20"},
        {"Alejandro", "22"},
        {"Carlos", "18"}
    };

    cout << "Alumnos + Calificación:" << endl;
    for (int i = 0; i < alumnos.size(); i++) {
        cout << "[" << i << "]: " << alumnos[i].toString() << endl;
    }
    return 0;
}
