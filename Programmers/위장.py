def solution(clothes):
    answer = 1
    c = {}
    
    for i in clothes:
        cloth = i[0]
        c_type = i[1]
        c[c_type] = c.get(c_type, []) + [cloth]
    
    print(len(c))
    
    for i in c:
        print(i)
        print(len(c[i]))
        answer = answer * (len(c[i]) + 1)
    
    answer = answer - 1
    return answer


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))