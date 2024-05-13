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

number = 2
result = binarySearch(M, number)

print(f"The value of {number} is in index [{result}].")
