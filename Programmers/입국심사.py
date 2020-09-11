def solution(n, times):
    answer = 0
    short = 1
    long = max(times) * n 
    mid = (short + long) // 2
    people = 0

    while(short <= long):
        people = 0
        mid = (short + long) // 2
        
        for t in times:
            people += mid // t
        
        if people < n:
            short = mid + 1
        else:
            long = mid - 1
            answer = mid
        
    return answer