# Top-down implementation using lists
import random


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while len(left) != 0:
        result.append(left[0])
        left = left[1:]

    while len(right) != 0:
        result.append(right[0])
        right = right[1:]

    return result


def merge_sort(array):
    """Sort an array using the merge sort algorithm."""
    if len(array) <= 1:
        return array

    left = []
    right = []

    for i, x in enumerate(array):
        if i < len(array) / 2:
            left.append(x)
        else:
            right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


j = [38, 27, 43, 3, 9, 82, 10]

ARRAY = random.sample(range(1, 1000), 50)
print(f"Before: {ARRAY}")
# ARRAY = [2, 5, 6, 4, 8, 3, 1, 9, 7]
print(f"After: {merge_sort(ARRAY)}")

# print(merge_sort(j))
