def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += list(number[i:])
            break
        
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)

    return answer

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