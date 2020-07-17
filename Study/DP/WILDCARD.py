cache = [[-1] * 4] * 4
W = "p*"
name = "p"

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
    
'''
def wildcard(W : str, name : str, w : int, s : int):
    #기저 사례 처리
    if cache[w][s] != -1:
        return cache[w][s]
    skip = 0
    
    while (s < len(name)) and (w < len(W)) and (W[w] == '?' or W[w] == S[s]):
        w += 1
        s += 1
        
    if w == len(W) and s == len(name):
        cache[w][s] = 1
        return 1
    
    if W[w] == '*':
        while s + skip <= len(name):
            skip += 1
            
            if wildcard(W, name, w + 1, s + skip):
                cache[w][s] = 1
                return 1
    
    cache[w][s] = 0
    return 0


if __name__ == "__main__":
    
    #Test case 1
    time = 3
    words = ["he?p", "*p*", "*bb*"]
    test = [3, 3, 1]
    case = [["help", "heap", "helpp"], ["help", "papa", "hellp"], ["babbbc"]]
    
    for i in range(time):
        for j in range(test[i]):
            wildcard(words[i], case[j], len(words[i]), len(case[j]))
            if cache[len(words[i])][len(case[j])]:
                print(case[j])
            cache = [[-1] * 101] * 101
'''            
                
'''
#Test case
3

he?p
3
help
heap
helpp

*p*
3
help
papa
hello

*bb*
1
babbbc
'''