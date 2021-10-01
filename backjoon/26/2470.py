import sys
from math import inf


def binary_search(arr):
    i = 0
    j = len(arr) - 1
    r = inf

    while i < j:
        tmp = arr[i] + arr[j]
        if tmp == 0:
            return arr[i], arr[j]
        if abs(tmp) < r:
            result = (arr[i], arr[j])
            r = abs(tmp)
        if tmp > 0:
            j -= 1
        else:
            i += 1

    return result


input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
result = binary_search(arr)

print(result[0], result[1])
