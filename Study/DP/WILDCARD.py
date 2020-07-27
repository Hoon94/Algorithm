cache = [[-1 for x in range(10)] for y in range(10)]
W = "*p*"
name = "help"

def wildcard(w : int, s : int):
    #기저 사례 처리
    if cache[w][s] != -1:
        return cache[w][s]
    skip = 0
    
    while (w < len(W)) and (s < len(name)) and (W[w] == '?' or W[w] == name[s]):
        w += 1
        s += 1
        
    if w == (len(W)):
        if s == len(name):
            cache[w][s] = 1
            return
        else:
            cache[w][s] = 0
            return
    
    if W[w] == '*':
        while s + skip <= len(name):
            skip += 1
            
            if wildcard(w + 1, s + skip):
                cache[w][s] = 1
                return
    
    cache[w][s] = 0
    return

wildcard(0, 0)
print(cache[len(W)][len(name)])
if cache[len(W)][len(name)] == 1:
    print(name)

print(cache)