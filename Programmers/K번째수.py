def solution(array, commands):
    answer = []
    
    for i in commands:
        answer.append(sorted(array[(i[0] - 1):i[1]])[(i[2] - 1)])
        
    return answer

if __name__ == "__main__":
    
    #Test case 1
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    #result [5, 6, 3]

    print(solution(array, commands))