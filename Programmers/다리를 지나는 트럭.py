def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0

    while q:
        sec += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
                
    return sec

if __name__ == "__main__":
    
    #Test case 1
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    #result 8

    '''
    #Test case 2
    bridge_length = 100
    weight = 100
    truck_weights = [10]
    #result 101

    #Test case 3
    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    #result 110
    '''

    print(solution(bridge_length, weight, truck_weights))