#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arrayNumeros;
    for (int i = 1; i <= 10; i++) arrayNumeros.push_back(i);

    cout << "Recorrido inicial:" << endl;
    for (int i = 0; i < arrayNumeros.size(); i++) {
        cout << "[" << i << "]: " << arrayNumeros[i] << endl;
    }

    cout << "Buscando el valor 8:" << endl;
    for (int i = 0; i < arrayNumeros.size(); i++) {
        if (arrayNumeros[i] == 8) {
            cout << "¡Encontrado! El valor 8 está en la posición " << i << endl;
            break;
        }
    }

    arrayNumeros.insert(arrayNumeros.begin() + 5, 22);

    cout << "Recorrido después de la inserción:" << endl;
    for (int i = 0; i < arrayNumeros.size(); i++) {
        cout << "[" << i << "]: " << arrayNumeros[i] << endl;
    }

    cout << "Recorrido inverso:" << endl;
    for (int i = arrayNumeros.size() - 1; i >= 0; i--) {
        cout << "[" << i << "]: " << arrayNumeros[i] << endl;
    }

    return 0;
}