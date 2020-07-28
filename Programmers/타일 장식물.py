def solution(N):
    rad_array = [1, 1]

    for i in range(2, N):
        rad_array.append(rad_array[-1] + rad_array[-2])
    
    answer = (rad_array[-2] + rad_array[-1] * 2) * 2

    return answer