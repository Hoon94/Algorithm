def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            answer = i + 1
        else:
            break
    
    return answer

if __name__ == "__main__":
    
    #Test case 1
    citations = [3, 0, 6, 1, 5]
    #result

    print(solution(citations))