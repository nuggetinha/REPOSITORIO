#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bucketSort(float a[], int n) {
    vector<float> buckets[n];

    for (int i = 0; i < n; i++) {
        int index = n * a[i];
        buckets[index].push_back(a[i]);
    }

    for (int i = 0; i < n; i++)
        sort(buckets[i].begin(), buckets[i].end());

    int k = 0;
    for (int i = 0; i < n; i++)
        for (float val : buckets[i])
            a[k++] = val;
}

void printArr(float a[], int n) {
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
}

int main() {
    float a[] = {0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Antes de ordenar:" << endl;
    printArr(a, n);
    bucketSort(a, n);
    cout << "Después de ordenar:" << endl;
    printArr(a, n);
    return 0;
}
