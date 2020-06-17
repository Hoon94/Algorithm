def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        cnt += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    
    return cnt
if __name__ == "__main__":
    
    #Test case 1
    people = [70, 50, 80, 50]
    limit = 100
    #result 3

    '''
    #Test case 2
    people = [70, 80, 50]
    limit = 100
    #result 3
    '''

    print(solution(people, limit))