def solution(n, lost, reserve):
    answer = 0
    
    s = set(lost) & set(reserve) # & 교집합
    l = set(lost) - s # - 차집합
    r = set(reserve) - s

    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)

    answer = n - len(l)

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