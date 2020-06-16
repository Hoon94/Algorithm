def solution(name):
    count = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {}
    indexes = []
    current_idx = 0
    n = len(name)

    for i in range(len(alpha)):
        d[alpha[i]] = min(i, 26 - i)
    
    for i in range(n):
        num = d[name[i]]
        count += num

        if num != 0:
            indexes.append(i)

    while True:
        if len(indexes) == 0:
            break

        min_dist = 99
        min_idx = 0

        for it in indexes:
            min_dist2 = min(abs(it - current_idx), n - abs(it - current_idx))

            if min_dist2 < min_dist:
                min_dist = min_dist2
                min_idx = it

        count += min_dist
        indexes.remove(min_idx)
        current_idx = min_idx

    return count

if __name__ == "__main__":
    
    #Test case 1
    name = "JEROEN"
    #result 56

    '''
    #Test case 2
    name = "JAN"
    #result 23
    '''

    print(solution(name))