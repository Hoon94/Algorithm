def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result

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