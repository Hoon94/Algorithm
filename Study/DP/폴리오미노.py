def poly(n : int, down : int):
    if down == n:
        return 1
    
    if cache[n][down] != -1:
        return cache[n][down]
    
    x = n - down
    ret = 0

    for o in range(1, x + 1):
        ret += (o + down - 1) * poly(x, o)
        ret %= 10000000
    cache[n][down] = ret
    return ret
 
if __name__ == "__main__":
    cache = [[-1 for j in range(101)] for k in range(101)]
    case = int(input())
    
    for i in range(case):
        num = int(input())
        result = 0
        for down in range(1, num + 1):
            result += poly(num, down)
            result %= 10000000
            
        print(result)