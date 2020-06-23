def solution(weight):
    weight = sorted(weight)
    answer = 1
    
    for w in weight:
        if answer >= w:
            answer += w
    
    return answer

if __name__ == "__main__":
    
    #Test case 1
    weight = [3, 1, 6, 2, 7, 30, 1]
    #result 21

    print(solution(weight))