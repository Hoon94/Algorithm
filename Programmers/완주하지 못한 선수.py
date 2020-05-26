def solution(participant, completion):
    answer = ''
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    
    dnf = [key for key, value in d.items() if value != 0]
    answer = dnf[0]

    return answer

if __name__ == "__main__":
    
    
    #Test case 1
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    #answer = "leo"
    

    '''
    #Test case 2
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]	
    completion = ["josipa", "filipa", "marina", "nikola"]
    #answer = "vinko"
    '''

    '''
    #Test case 3
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    #answer = "mislav"
    '''
    
    print(solution(participant, completion))