from copy import deepcopy

N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

arr = [[0] * M for _ in range(N)]
wall = deepcopy(arr)

wall[0][0] = 1

print(wall)
print(arr)