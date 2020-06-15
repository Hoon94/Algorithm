def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1

        if f in _lost:
            _lost.remove(f)

        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)

if __name__ == "__main__":
    
    #Test case 1
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    #answer = 5

'''
    #Test case 2
    n = 5
    lost = [2, 4]
    reserve = [3]
    #answer = 4

    #Test case 3
    n = 3
    lost = [3]
    reserve = [1]
    #answer = 2
'''

print(solution(n, lost, reserve))