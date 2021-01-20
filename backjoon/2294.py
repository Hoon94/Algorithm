import sys
input = sys.stdin.readline

if __name__ == "__main__":

    n, k = map(int, input().split())
    coins = sorted([int(input()) for _ in range(n)])

    arr = [10001] * (k + 1)
    arr[0] = 0

    for i in range(n):
        for j in range(coins[i], k + 1):
            arr[j] = min(arr[j], arr[j - coins[i]] + 1)

    arr[-1] = arr[-1] if arr[-1] != 10001 else -1
    print(arr[-1])