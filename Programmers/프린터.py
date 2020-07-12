def solution(priorities, location):
    pos = []

    for i in range(len(priorities)):
        if i == location:
            pos.append(True)
        else:
            pos.append(False)
            
    count = 0
    m = max(priorities)

    while True:
        if m > priorities[0]:
            priorities.append(priorities.pop(0))
            pos.append(pos.pop(0))
        else:
            count += 1
            priorities.pop(0)
            if pos.pop(0):
                return count
            m = max(priorities)

if __name__ == "__main__":
    
    #Test case 1
    priorities = [2, 1, 3, 2]
    location = 2
    #result 1

    '''
    #Test case 2
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    #result 5
    '''

    print(solution(priorities, location))