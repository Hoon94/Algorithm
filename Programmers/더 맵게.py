import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)

        if n1 < K or n2 < K :
            heapq.heappush(scoville, n1 + (n2 * 2))
            count += 1
        else :
            return count

    if scoville[0] > K:
        return count
    else :
        return -1

if __name__ == "__main__":
    
    #Test case 1
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    #result 2

    print(solution(scoville, K))