def solution(baseball):
    answer = 0
    
    for i in range(123, 988):
        x = int(str(i)[0])
        y = int(str(i)[1])
        z = int(str(i)[2])
        
        if x == 0 or y == 0 or z == 0:
            continue
        if x == y or y == z or z == x:
            continue
            
        for i, (num, s, b) in enumerate(baseball):
            baseX = int(str(num)[0])
            baseY = int(str(num)[1])
            baseZ = int(str(num)[2])
            strike = 0
            ball = 0
            
            if baseX == x:
                strike += 1
            if baseY == y:
                strike += 1
            if baseZ == z:
                strike += 1
            if strike != s:
                break
            
            if baseY == x or baseZ == x:
                ball += 1
            if baseX == y or baseZ == y:
                ball += 1
            if baseX == z or baseY == z:
                ball += 1
            if ball != b:
                break
                
            if i == len(baseball) - 1:
                answer += 1
    
    return answer

if __name__ == "__main__":
    
    #Test case 1
    baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    #result 2

    print(solution(baseball))