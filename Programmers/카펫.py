def solution(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow // i + 2, i + 2]
                
if __name__ == "__main__":
    
    #Test case 1
    brown = 10
    yellow = 2
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