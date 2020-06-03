def dfs(numbers, target):
    if len(numbers) == 1 and target == numbers[0]:
        return 1
    elif len(numbers) == 1 and target == -numbers[0]:
        return 1
    elif len(numbers) == 1:
        return 0
    
    return dfs(numbers[1:], target - numbers[0]) + dfs(numbers[1:], target + numbers[0])

def solution(numbers, target):
    answer = 0
    
    answer = dfs(numbers[1:], target - numbers[0]) + dfs(numbers[1:], target + numbers[0])
    
    return answer

if __name__ == "__main__":
    
    #Test case 1
    numbers = [1, 1, 1, 1, 1]
    target = 3
    #result 5
    '''
    #Test case 2
    numbers = [1, 1]
    target = 2
    #result 1
    '''
    print(solution(numbers, target))