n = int(input())
sequence = list(map(int, input().split()))
length = len(sequence)


def binary_search(start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if sequence[mid] == mid:
        return mid
    elif sequence[mid] > mid:
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)


if sequence[-1] == length - 1:
    print(length - 1)
else:
    result = binary_search(0, length - 1)
    print(result)
