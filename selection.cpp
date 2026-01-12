#include <iostream>
using namespace std;

void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        }
        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
}

void printArr(int a[], int n) {
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[] = {70, 15, 2, 51, 60};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Antes de ordenar:" << endl;
    printArr(a, n);
    selectionSort(a, n);
    cout << "Después de ordenar:" << endl;
    printArr(a, n);
    return 0;
}
