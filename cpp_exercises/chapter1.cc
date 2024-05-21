#include <iostream>
#include <limits>

using namespace std;

int main() {
    long double a = 2147483647;
    char b = 2;
    short int c;

    cout << "Tamanho do long double " << sizeof(a) << '\n';
    cout << "Tamanho do char " << sizeof(b) << '\n';
    cout << "Tamanho do short int " << sizeof(c) << '\n';
    cout << "Max value of type int is " << numeric_limits<long double>::max();


    return 0;

}
