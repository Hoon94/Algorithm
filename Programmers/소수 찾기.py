from itertools import permutations

def solution(n):
    a = set()

    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    
    a -= set(range(0, 2))
    
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    
    return len(a)

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