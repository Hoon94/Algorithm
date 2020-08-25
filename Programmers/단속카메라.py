def solution(routes):
    routes = sorted(routes, key = lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

if __name__ == "__main__":
    
    #Test case 1
    routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    #result 2

    print(solution(routes))