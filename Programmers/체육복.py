def solution(n, lost, reserve):
    answer = 0
    uniform = [1] * (n + 2)

    for i in reserve:
        uniform[i] += 1

    for i in lost:
        uniform[i] -= 1
    
    for i in range(1, n + 1):
        if uniform[i - 1] == 0 and uniform[i] == 2:
            uniform[i - 1:i + 1] = [1, 1]
        elif uniform[i] == 2 and uniform[i + 1] == 0:
            uniform[i:i + 2] = [1, 1]

    answer = len([x for x in uniform[1:-1] if x > 0])

    return answer


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