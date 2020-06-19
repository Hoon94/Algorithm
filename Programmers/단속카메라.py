def solution(routes):
    answer = 0
    routes.sort()

    standard = routes[0][1]
    routes.pop(0)
    answer += 1

    for item in routes:
        if item[0] <= standard:
            standard = min(item[1], standard)
        else:
            standard = item[1]
            answer += 1
            
    return answer

if __name__ == "__main__":
    
    #Test case 1
    routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    #result 2

    print(solution(routes))