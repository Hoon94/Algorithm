from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
answer = float('INF')
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

for combos in combinations(chicken, m):
    total = 0
    for home in house:
        total += min([abs(home[0] - combo[0]) +
                      abs(home[1] - combo[1]) for combo in combos])
        if answer <= total:
            break

    answer = min(answer, total)

print(answer)
