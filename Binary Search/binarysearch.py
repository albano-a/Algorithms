import numpy as np


def binarySearch(A, T):
    n = len(A)
    L = 0
    R = n - 1

    while L <= R:
        m = int(((L + R) / 2))
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m

    return "Unsuccessful"


# Example
M = np.arange(1, 10, 1)
N = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

number = 2
letter = "h"

result = binarySearch(M, number)
result_2 = binarySearch(N, letter)

print(f"The value of {number} is in index [{result}].")
print(f"The value of {letter} is in index [{result_2}].")
