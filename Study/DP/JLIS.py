#cache = [[-1] * 101] * 101
'''
A = [1, 2, 3]
B = [4, 5, 6]
'''
A = [10, 20, 30, 1, 2]
B = [10, 20, 30]

n = 5 #len(A)
m = 3 #len(B)
cache = [[-1 for col in range(m + 1)] for row in range(n + 1)]

def jlis(indexA : int, indexB : int):
    print(indexA, indexB)
    if cache[indexA + 1][indexB + 1] != -1:
        return cache[indexA + 1][indexB + 1]
    
    cache[indexA + 1][indexB + 1] = 2
    
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
            print('nextA : ', nextA, 'indexB : ', indexB, 'value : ', cache[indexA + 1][indexB + 1])
        nextA += 1
    
    nextB = indexB + 1
    while nextB < m:
        if maxElement < B[nextB]:
            cache[indexA + 1][indexB + 1] = max(cache[indexA + 1][indexB + 1], jlis(indexA, nextB) + 1)
            print('indexA : ', indexA, 'nextB : ', nextB, 'value : ', cache[indexA + 1][indexB + 1])
        nextB += 1
        
    return cache[indexA + 1][indexB + 1]

print(cache)
print(jlis(-1, -1))