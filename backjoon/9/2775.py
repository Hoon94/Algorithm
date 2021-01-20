T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    base = [j for j in range(1, n+1)]
    for l in range(k):
        for m in range(1, n):
            base[m] += base[m-1]
    print(base[n-1])

'''
재귀의 경우 시간 초과 발생

test = int(input())

def num(a : int, b : int):
    s = 0
    
    if a == 0:
        return b
    
    for i in range(1, b+1):
        s += num(a-1, i)

    return s

for i in range(test):
    k = int(input())
    n = int(input())

    members = num(k, n)
    print(members)

'''