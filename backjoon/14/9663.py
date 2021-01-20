from sys

def dfs(x):
    global answer

    if x == n:
        answer += 1
        return

    for y in range(n):
        if y in columns or (x + y) in l_diagonals or (x - y) in r_diagonals:
            continue
        
        columns.add(y)
        l_diagonals.add(x + y)
        r_diagonals.add(x - y)
        dfs(x + 1)
        columns.remove(y)
        l_diagonals.remove(x + y)
        r_diagonals.remove(x - y)


if __name__ == '__main__':
    answer = 0
    n = int(sys.stdin.readline())
    columns, l_diagonals, r_diagonals = set(), set(), set()
    dfs(0)
    print(answer)