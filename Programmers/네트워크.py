from collections import deque
def bfs(x, y, computers, start, n):
    nx = [-1, 0, 1, 0]
    ny = [0, 1, 0, -1]
    
    computers[x][y] = 0
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        
        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            continue
        if computers[dx][dy]:
            bfs(dx, dy, computers, start, n)

def solution(n, computers):
    answer = 0
    start = deque()    
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                start.append([i, j])
    
    while len(start) != 0:
        x, y = start.popleft()
        if computers[x][y]:
            answer += 1
            bfs(x, y, computers, start, n)
    
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