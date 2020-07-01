def solution(brown, yellow):
    whole = brown + yellow
    available_lst = []

    for w in range(3, whole // 3+1):
        if whole % w == 0 and w <= whole/w:
            available_lst.append([int(whole / w), w])
            
    for avail in available_lst:
        if sum(avail) * 2 - 4 == brown:
            answer = avail
    return answer

if __name__ == "__main__":
    
    #Test case 1
    brown = 10
    yellow = 8
    #result [4, 3]

    '''
    #Test case 2
    brown = 8
    yellow = 1
    #result[3, 3]
    
    #Test case 3
    brown = 24
    yellow = 24
    #result [8, 6]
    '''

    print(solution(brown, yellow))