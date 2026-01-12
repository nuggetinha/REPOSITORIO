#include <iostream>
using namespace std;

int getMax(int a[], int n) {
    int max = a[0];
    for (int i = 1; i < n; i++)
        if (a[i] > max)
            max = a[i];
    return max;
}

void countingSort(int a[], int n, int exp) {
    int output[n];
    int count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(a[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        int index = (a[i] / exp) % 10;
        output[count[index] - 1] = a[i];
        count[index]--;
    }

    for (int i = 0; i < n; i++)
        a[i] = output[i];
}

void radixSort(int a[], int n) {
    int max = getMax(a, n);
    for (int exp = 1; max / exp > 0; exp *= 10)
        countingSort(a, n, exp);
}

void printArr(int a[], int n) {
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Antes de ordenar:" << endl;
    printArr(a, n);
    radixSort(a, n);
    cout << "Después de ordenar:" << endl;
    printArr(a, n);
    return 0;
}
