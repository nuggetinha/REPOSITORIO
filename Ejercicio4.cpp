#include <iostream>
using namespace std;

int main() {
    int matriz[3][3] = {
        {10, 20, 30},
        {40, 50, 60},
        {70, 80, 90}
    };

    cout << "Matriz" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }

    cout << "Horizontal" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "[" << i << "][" << j << "]: " << matriz[i][j] << endl;
        }
    }

    cout << "Vertical" << endl;
    for (int j = 0; j < 3; j++) {
        for (int i = 0; i < 3; i++) {
            cout << "[" << i << "][" << j << "]: " << matriz[i][j] << endl;
        }
    }

    return 0;
}
