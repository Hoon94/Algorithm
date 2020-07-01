def solution(brown, red):
    for index in range(1, red + 1):
        if red % index == 0: 
            length = red // index
            if (((index + 2) * (length + 2)) - (index * length)) == brown:
                return [max(index + 2, length + 2), min(index + 2, length + 2)]

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