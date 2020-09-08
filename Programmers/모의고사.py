from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

if __name__ == "__main__":
    
    #Test case 1
    answers = [1, 2, 3, 4, 5]
    #result [1]

    '''
    #Test case 2
    answers = [1, 3, 2, 4, 2]
    #result [1, 2, 3]
    '''

    print(solution(answers))