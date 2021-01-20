if __name__ == "__main__":

    n, k = map(int, input().split())
    cache = []

    for i in range(n + 1):
        cache.append([1] * (i + 1))

    for i in range(2, n + 1):
        for j in range(1, i):
            cache[i][j] = (cache[i - 1][j - 1] + cache[i - 1][j]) % 10007

    print(cache[n][k])