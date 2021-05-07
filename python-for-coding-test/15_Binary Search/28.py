def binary_search(sequence, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if sequence[mid] == mid:
        return mid
    elif sequence[mid] > mid:
        return binary_search(sequence, start, mid - 1)
    else:
        return binary_search(sequence, mid + 1, end)


n = int(input())
sequence = list(map(int, input().split()))

result = binary_search(sequence, 0, n - 1)
print(result)
