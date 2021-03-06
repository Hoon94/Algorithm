# 치킨집 선정
def find(idx, x, y):
    global ans

    if(idx == m):
        r = []
        for i in range(n):
            for j in range(n):
                if(arr[i][j] == 3):
                    r.append((i, j))
        res = far(r, house)
        if(ans > sum(res)):
            ans = sum(res)
        return
    else:
        for i in range(x, n):
            if(i == x):
                k = y
            else:
                k = 0
            for j in range(k, n):
                if(arr[i][j] == 2):
                    arr[i][j] = 3
                    find(idx + 1, i, j + 1)
                    arr[i][j] = 2


# 도시의 치킨거리 구해주기
def far(c, h):
    res = []

    for i in h:
        minV = 999999
        for j in c:
            fars = abs(i[0] - j[0]) + abs(i[1] - j[1]) 
            minV = min(minV, fars)
        res.append(minV)
    
    return res

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 99999

    # 0 = 빈칸 // 1 = 집 // 2 = 치킨집
    # 집 찾기, 치킨집 개수 찾기
    chicken = 0
    house = []
    for i in range(n):
        for j in range(n):
            if(arr[i][j] == 1):
                house.append((i, j))
            elif(arr[i][j] == 2):
                chicken += 1

    find(0, 0, 0)
    print(ans)