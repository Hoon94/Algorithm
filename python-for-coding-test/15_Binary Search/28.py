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


n = int(input())
sequence = list(map(int, input().split()))

if sequence[-1] == n - 1:
    print(n - 1)
else:
    result = binary_search(0, n - 1)
    print(result)
