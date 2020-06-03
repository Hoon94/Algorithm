def solution(numbers, target):    
    if len(numbers) == 1 and target == numbers[0]:
        return 1
    elif len(numbers) == 1 and target == -numbers[0]:
        return 1
    elif len(numbers) == 1:
        return 0

    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

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