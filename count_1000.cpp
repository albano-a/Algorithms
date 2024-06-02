#include <iostream>
#include <chrono>

using namespace std;

int main(){
    auto start = chrono::high_resolution_clock::now();

    int count = 0;

    for (long long int i = 0; i < 1'000'000'000'000; ++i) {
        count += 1;
    }

    auto end = chrono::high_resolution_clock::now();

    // Duration
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);

    cout << "We reached " << count << " iterations" << "\n";
    cout << "Time taken: " << duration.count() << "ms\n";
}