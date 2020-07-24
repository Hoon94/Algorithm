cache = [-1] * 10

def classify(a : int, b : int):
    M = list(map(int, N[a:b]))
    print(M)
    
    if M == M[0] * len(M):
        return 1

    progressive = True
    
    for i in range(len(M) - 1):
        if M[i + 1] - M[i] != M[1] - M[0]:
            progressive = False
            break

    if progressive and abs(M[1] - M[0]) == 1:
        return 2

    alternating = True
    for i in range(len(M)):
        if M[i] != M[i % 2]:
            alternating = False

    if alternating:
        return 4

    if progressive:
        return 5

    return 10

def memorize(begin : int):
    if begin == len(N):
        return 0
    
    if cache[begin] != -1:
        return cache[begin]

    cache[begin] = 10000
    for L in range(3, 6):
        if begin + L <= len(N):
            cache[begin] = min(cache[begin], memorize(begin + L) + classify(begin, begin + L))

    return cache[begin]

#N = '12341234' # 4
#N = '11111222' # 2
#N = '12122222' # 5
#N = '22222222' # 2
N = '12673939' # 14

print(memorize(0))
print(cache)