from itertools import permutations

def solution(numbers):
    answer = set()
    maximum = 10000000
    prime_lst = [False, False] + [True] * maximum

    for idx, num in enumerate(prime_lst):
        if num:
            k = idx * 2
            while k <= maximum:
                prime_lst[k] = False
                k += idx

    for i in range(1, len(numbers) + 1):
        perm = permutations(list(numbers), i)
        for i in list(perm):
            num = int("".join(list(i)))
            if prime_lst[num]:
                answer.add(num)

    return len(answer)

if __name__ == "__main__":
    
    #Test case 1
    numbers = "17"
    #result 3

    '''
    #Test case 2
    numbers = "011"
    #result 2
    '''

    print(solution(numbers))