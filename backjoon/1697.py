import sys
from collections import deque

def solve(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()

        if i == k:
            return arr[i]

        for j in (i + 1, i - 1, 2 * i):
            if (0 <= j < LIMIT) and arr[j] == 0:
                arr[j] = arr[i] + 1
                q.append(j)

if __name__ == "__main__":
    LIMIT = 100001

    N, K = map(int, sys.stdin.readline().split())
    find = [0] * LIMIT

    print(solve(find, N, K))