def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer

if __name__ == "__main__":
    
    #Test case 1
    prices = [1, 2, 3, 2, 3]
    #result [4, 3, 1, 1, 0]

    print(solution(prices))