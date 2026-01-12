#include <iostream>
using namespace std;

int main() {
    int array[] = {11, 12, 13, 14, 15};

    cout << "Array: ";
    for (int num : array) {
        cout << num << " ";
    }
    return 0;
}