def solution(number, k):

    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()

        stack.append(num)
    
    #두 코드 차이점
    #enumerate를 사용하지 않는 경우에는 끝까지 for문으로 확인해야 한다.

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)

if __name__ == "__main__":
    
    #Test case 1
    number = "1924"
    k = 2
    #result "94"

    '''
    #Test case 2
    number = "1231234"
    k = 3
    #result "3234"
    '''

    '''
    #Test case 3
    number = "4177252841"
    k = 4
    #result "775841"
    '''

    print(solution(number, k))