def solution(clothes):
    answer = 1
    c = {}
    
    for i in clothes:
        cloth = i[0]
        c_type = i[1]
        c[c_type] = c.get(c_type, []) + [cloth]
    
    for i in c:
        answer = answer * (len(c[i]) + 1)
    
    answer = answer - 1
    return answer

if __name__ == "__main__":
    
    #Test case 1
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    #result 5
    
    '''
    #Test case 2
    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    #reslt 3
    '''

    print(solution(clothes))