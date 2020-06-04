from collections import deque
def bfs(queue, visited, target, words):
    while len(queue):
        start = queue.popleft()
        if start != target:
            for word in words:
                cnt = 0
                for i in range(len(start)):
                    if start[i] != word[i]:
                        cnt += 1
                if cnt == 1 and word not in visited:
                    queue.append(word)
                    visited.append(word)            
    
def solution(begin, target, words):
    answer = 0
    visited = [begin]
    queue = deque([begin])
    
    while len(queue):
        begin = queue.popleft()
        if begin != target:
            for word in words:
                cnt = 0
                for i in range(len(begin)):
                    if begin[i] != word[i]:
                        cnt += 1
                if cnt == 1 and word not in visited:
                    queue.append(word)
                    visited.append(word)
                    
            bfs(queue, visited, target, words)

    if target == visited[-1]:
        return len(visited) - 1
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