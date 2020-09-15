import sys

def solve_dfs(i):
    global ans

    if i == n:
        ans += 1
        return

    for j in range(n):
        if (not a[j] and not b[i + j] and not c[i - j + n - 1]) :
            a[j] = b[i + j] = c[i - j + n - 1] = True
            solve_dfs(i + 1)
            a[j] = b[i + j] = c[i - j + n - 1] = False

if __name__ == "__main__":
    
    n = int(sys.stdin.readline())
    ans = 0
    a = [False] * n
    b = [False] * (2 * (n - 1))
    c = [False] * (2 * (n - 1))

    solve_dfs(0)
    
    print(ans)