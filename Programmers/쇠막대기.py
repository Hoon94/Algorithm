def solution(arrangment):
    arrangement = arrangment.replace("()", "0")
    x = 0
    cnt = 0
    
    for e in arrangement:
        if e == "(":
            x += 1
            cnt += 1
        elif e == "0":
            cnt += x
        else:
            x -= 1

    return cnt