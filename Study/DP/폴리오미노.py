def poly(n, d):
    if d == n:
        return 1
    
    if board[n][d] != -1:
        return board[n][d]
    
    x = n - d
    ret = 0

    for o in range(1, x + 1):
        ret += (o + d - 1) * poly(x, o)
        ret %= 10000000
    board[n][d] = ret
    return ret
 
if __name__ == "__main__":
    board = [[-1 for j in range(101)] for k in range(101)]
    case = int(input())
    
    for i in range(case):
        num = int(input())
        result = 0
        for down in range(1, num + 1):
            result += poly(num, down)
            result %= 10000000
            
        print(result)