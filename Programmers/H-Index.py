def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))

    return answer

if __name__ == "__main__":
    
    #Test case 1
    citations = [3, 0, 6, 1, 5]
    #result

    print(solution(citations))