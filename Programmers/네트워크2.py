def dfs(x, y, computers, n):
    computers[x][y] = 0
    computers[y][x] = 0
    
    for i in range(n):
        if computers[y][i]:
            dfs(y, i, computers, n)
    
def solution(n, computers):
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                dfs(i, j, computers, n)
                answer += 1
    return answer

if __name__ == "__main__":
    
    #Test case 1
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    #result 2

    '''
    #Test case 2
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    #result 1
    '''

    print(solution(n, computers))