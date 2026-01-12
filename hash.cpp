#include <iostream>
#include <vector>
using namespace std;

vector<int> hashSort(int a[], int n) {
    int maxVal = a[0];
    for (int i = 1; i < n; i++)
        if (a[i] > maxVal) maxVal = a[i];

    vector<int> hashTable(maxVal + 1, 0);

    for (int i = 0; i < n; i++)
        hashTable[a[i]] = 1;

    vector<int> sorted;
    for (int i = 0; i <= maxVal; i++)
        if (hashTable[i] == 1)
            sorted.push_back(i);

    return sorted;
}

int main() {
    int a[] = {70, 15, 2, 51, 60};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Antes de ordenar:" << endl;
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;

    vector<int> sorted = hashSort(a, n);

    cout << "Después de ordenar:" << endl;
    for (int x : sorted) cout << x << " ";
    cout << endl;
    return 0;
}
