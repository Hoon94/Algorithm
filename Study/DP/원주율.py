def classify(a : int, b : int):
    M = list(map(int, N[a:b]))
    
    if M == [M[0]] * len(M):
        return 1

    progressive = True
    
    for i in range(len(M) - 1):
        if M[i + 1] - M[i] != M[1] - M[0]:
            progressive = False
            break

    if progressive and abs(M[1] - M[0]) == 1:
        return 2
    elif progressive:
        return 5

    alternating = True
    for i in range(len(M)):
        if M[i] != M[(i % 2)]:
            alternating = False

    if alternating:
        return 4

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

if __name__ == "__main__":
    C = int(input("Number of Test case : "))
    Ns = ['12341234', '11111222', '12122222', '22222222', '12673939']

    for i in range(C):
        cache = [-1] * 10
        N = Ns[i]

        print(memorize(0))

    #Result = 4, 2, 5, 2, 14