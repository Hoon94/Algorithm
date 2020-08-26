def solution(scoville, K):
    answer = -1 
    count = 0 
    check_flag = False 
    
    while min(scoville) < K:
        scoville = sorted(scoville, reverse = True)
        scoville.append(scoville.pop() + (scoville.pop() * 2)) 
        
        if len(scoville) == 1 and scoville[0] < K:
            check_flag = True
            break
        
        count += 1
        
    if check_flag == False:
        answer = count
        
    return answer