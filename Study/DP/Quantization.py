def saveSum(num : list):
    num = sorted(num)

    pSum[0] = num[0]
    pSqSum[0] = num[0] ** 2
    for i in range(1, n):
        pSum[i] = pSum[i - 1] + num[i]
        pSqSum[i] = pSqSum[i - 1] + (num[i] ** 2)
    
    return num

def minError(low : int, high : int):
    if low == 0:
        Sum = pSum[high]
        sqSum = pSqSum[high]
    else:
        Sum = pSum[high] - pSum[low - 1]
        sqSum = pSqSum[high] - pSqSum[low - 1]

    m = round(Sum / (high - low + 1))
    ret = sqSum - (2 * m * Sum) + (m * m * (high - low + 1))

    return ret

def quantize(start : int, parts : int):
    if start == n:
        return 0

    if parts == 0:
        return 10000
    
    if cache[start][parts] != -1:
        return cache[start][parts]
    
    cache[start][parts] = 10000

    for partsize in range(1, (n - start + 1)):
        cache[start][parts] = min(cache[start][parts], minError(start, start + partsize - 1) + quantize(start + partsize, parts - 1))

    return cache[start][parts]

if __name__ == "__main__":
    pSum = [0] * 101
    pSqSum = [0] * 101
    cache= [[-1 for x in range(11)] for y in range(11)]

    n = 10
    s = 3
    num = [3, 3, 3, 1, 2, 3, 2, 2, 2, 1]
    
    '''
    n = 9
    s = 3
    num = [1, 744, 755, 4, 897, 902, 890, 6, 777]
    '''

    num = saveSum(num)
    print(quantize(0, s))