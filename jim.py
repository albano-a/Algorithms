def bitap_search(text: str, pattern: str) -> str:
    m = len(pattern)

    if m == 0:
        return text

    # Initialize the bit array R.
    R = [0] * (m + 1)
    R[0] = 1

    for i in range(0, len(text)):
        # Update the bit array
        for k in range(m, 0, -1):
            R[k] = R[k - 1] & (text[i] == pattern[k - 1])

        if R[m]:
            return i - m + 1

    return -1

a = bitap_search("hello world", "world")  # 6
print(a)