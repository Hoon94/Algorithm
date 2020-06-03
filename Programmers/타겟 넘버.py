def solution(numbers, target):
    answer = 0
    first = len(numbers)
    
    def dfs(start, numbers):
        if len(numbers) == 0:
            return 0
        
        result = result + dfs(numbers[0], numbers[1:])
        if len(numbers) == first and result == target:
            answer += 1
        result = result + dfs(-numbers[0], numbers[1:])
        if len(numbers) == first and result == target:
            answer += 1

    dfs(numbers[0], numbers[1:])
    
    return answer

if __name__ == "__main__":
    '''
    #Test case 1
    numbers = [1, 1, 1, 1, 1]
    target = 3
    #result 5
    '''
    #Test case 2
    numbers = [1, 1]
    target = 2
    #result 1

    solution(numbers, target)