""" Implements the quicksort algorithm """

import random


# Sorts a (portion of an) array, divides it into partitions, then sorts those
def quicksort(A, lo, hi):
    """Implements the Lomuto partition scheme for Quick Sort algorithm"""
    # Ensure indices are in correct order
    if lo >= hi or lo < 0:
        return "Undefined"

    # Partition array and get the pivot index
    p = partition(A, lo, hi)

    # Sort the two partitions
    quicksort(A, lo, p - 1)  # Left side of pivot
    quicksort(A, p + 1, hi)  # Right side of pivot

    return A


def partition(A, lo, hi):
    """Partition the array"""
    pivot = A[hi]  # Choose the last element as the pivot
    # Temporary pivot index
    i = lo
    for j in range(lo, hi):
        # If the current element is less than or equal to the pivot
        if A[j] <= pivot:
            # Swap the current element with the element at the temporary pivot index
            A[i], A[j] = A[j], A[i]
            # Move the temporary pivot index forward
            i = i + 1

    # Swap the pivot with the last element
    A[i], A[hi] = A[hi], A[i]
    return i  # the pivot index


ARRAY = random.sample(range(1, 1000), 500)
# ARRAY = [2, 5, 6, 4, 8, 3, 1, 9, 7]
print(quicksort(ARRAY, 0, len(ARRAY) - 1))
