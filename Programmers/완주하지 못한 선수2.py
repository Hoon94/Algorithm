def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

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