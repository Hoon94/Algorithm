def jlis(indexA : int, indexB : int):
    if cache[indexA + 1][indexB + 1] != -1:
        return cache[indexA + 1][indexB + 1]

    cache[indexA + 1][indexB + 1] = 0
    
    if indexA == -1:
        a = -100
    else:
        a = A[indexA]
        
    if indexB == -1:
        b = -100
    else:
        b = B[indexB]
    
    maxElement = max(a, b)
    
    nextA = indexA + 1
    while nextA < n:
        if maxElement < A[nextA]:
            cache[indexA + 1][indexB + 1] = max(cache[indexA + 1][indexB + 1], jlis(nextA, indexB) + 1)
        nextA += 1

    nextB = indexB + 1
    while nextB < m:
        if maxElement < B[nextB]:
            cache[indexA + 1][indexB + 1] = max(cache[indexA + 1][indexB + 1], jlis(indexA, nextB) + 1)
        nextB += 1
        
    return cache[indexA + 1][indexB + 1]

if __name__ == "__main__":
    C = int(input("Number of Test case : "))
    ns = [3, 3, 5]
    ms = [3, 3, 3]
    As = [[1, 2, 4], [1, 2, 3], [10, 20, 30, 1, 2]]
    Bs = [[3, 4, 7], [4, 5, 6], [10, 20, 30]]

    for i in range(C):
        A = As[i]; B = Bs[i]
        n = ns[i]; m = ms[i]

        cache = [[-1 for col in range(m + 1)] for row in range(n + 1)]

        print(jlis(-1, -1))

    #Result = 5, 6, 5