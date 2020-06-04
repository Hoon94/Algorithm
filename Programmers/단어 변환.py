from collections import deque
def bfs(queue, visited, words):
    result = 0

    while len(queue):
        start = queue.popleft()
        for i in range(len(words)):
            cnt = 0
            if start == target:
                break
            else:
                for j in range(len(target)):
                    if start[j] != words[i][j]:
                        cnt += 1
                if cnt == 1 and i not in visited:
                    result += 1
                    visited.append(i)
                    queue.append(words[i])

    return result


def solution(begin, target, words):
    answer = 0
    visited = []
    queue = deque([begin])

    for i in range(len(words)):
        cnt = 0
        if begin == target:
            break
        else:
            for j in range(len(target)):
                if begin[j] != words[i][j]:
                    cnt += 1
            if cnt == 1 and i not in visited:
                visited.append(i)
                queue.append(words[i])
    answer = bfs(queue, visited, words)

    print(visited)
    return answer

if __name__ == "__main__":
    
    #Test case 1
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    #result 4

    '''
    #Test case 2
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    #result 0
    '''

    print(solution(begin, target, words))