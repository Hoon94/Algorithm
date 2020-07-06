def solution(heights):
    answer = []

    for s_idx in range(len(heights) - 1, -1, -1):
        flag = False
        for r_idx in range(s_idx - 1, -1, -1):
            if heights[s_idx] < heights[r_idx]:
                flag = True
                answer = [r_idx + 1] + answer
                break
        if not flag:
            answer = [0] + answer
            
    return answer

if __name__ == "__main__":
    
    #Test case 1
    heights = [6, 9, 5, 7, 4]
    #result [0, 0, 2, 2, 4]

    '''
    #Test case 2
    heights = [3, 9, 9, 3, 5, 7, 2]
    #result [0, 0, 0, 3, 3, 3, 6]

    #Test case 3
    heights = [1, 5, 3, 6, 7, 6, 5]
    #result [0, 0, 2, 0, 0, 5, 6]
    '''

    print(solution(heights))