def solution(priorities, location):
    queue =  [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

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