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
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))