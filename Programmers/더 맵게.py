import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0

    while True:
        first = hq.heappop(scoville)

        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1  

    return answer

if __name__ == "__main__":
    
    #Test case 1
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    #result 2

    print(solution(scoville, K))