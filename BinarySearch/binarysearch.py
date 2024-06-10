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


LOW = 1
HIGH = 100

# Example
M = np.arange(LOW, HIGH, 1)

number = np.random.randint(LOW, HIGH)

result = binarySearch(M, number)

print(f"The value of {number} is in index {result}.")
