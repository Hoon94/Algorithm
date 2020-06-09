def solution(citations):
    answer = 0
    
    citations.sort()
    l = len(citations)

    for i in range(l):
        if l - i <= citations[i]:
            return l - i
    
    return answer

if __name__ == "__main__":
    
    #Test case 1
    citations = [3, 0, 6, 1, 5]
    #result

    print(solution(citations))