#include <iostream>
using namespace std;

template <typename T>
const char* evenodd(T a) {
    return (a % 2 == 0) ? "Even" : "odd";
}

int main() {
    cout << evenodd<int>(10) << endl;
    cout << evenodd<int>(7) << endl;
    return 0;
}

