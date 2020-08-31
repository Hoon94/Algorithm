MAX = 2000000001
cacheLen = [-1] * 501
cacheCnt = [-1] * 501
n = 8
k = 6
S = [5, 1, 6, 4, 3, 2, 8, 7]
lis = []

def solve(start):
    if cacheLen[start + 1] != -1:
        return cacheLen[start + 1]

    cacheLen[start + 1] = 1

    for next in range(start + 1, n):
        if start == -1 or S[start] < S[next]:
            cacheLen[start + 1] = max(cacheLen[start + 1], solve(next) + 1)
    
    return cacheLen[start + 1]

def count(start):
    if solve(start) == 1:
        return 1

    if cacheCnt[start + 1] != -1:
        return cacheCnt[start + 1]

    cacheCnt[start + 1] = 0

    for next in range(start + 1, n):
        if (start == -1 or S[start] < S[next]) and solve(start) == solve(next) + 1:
            cacheCnt[start + 1] = min(MAX, cacheCnt[start + 1] + count(next))

    return cacheCnt[start + 1]

def reconstruct(start, skip, lis):
    if start != -1:
        lis.append(S[start])

    followers = []

    for next in range(start + 1, n):
        if (start == -1 or S[start] < S[next]) and solve(start) == solve(next) + 1:
            followers.append([S[next], next])

    followers.sort()

    for i in range(len(followers)):
        num = followers[i][1]
        cnt = count(num)
        if skip >= cnt:
            skip -= cnt
        else:
            reconstruct(num, skip, lis)
            break


print(solve(-1) - 1)
skip = k - 1
reconstruct(-1, skip, lis)

for i in range(len(lis)):
    print(lis[i], end= ' ')