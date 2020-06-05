def solution(numbers):
    answer = ''
    numbers = sorted([str(x) for x in numbers], key= lambda x : (x * 4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = numbers[0]
    else:
        answer = ''.join(numbers)
    return answer

if __name__ == "__main__":
    
    #Test case 1
    numbers = [6, 10, 2]
    #result 

    '''
    #Test case 2
    numbers = [3, 30, 34, 5, 9]
    #result 
    '''

    print(solution(numbers))