visited = []

def dfs(tickets, start):
    global visited
    for i in tickets:
        if i[0] == start and i not in visited:
            visited.append(i)
            dfs(tickets, i[1])

def solution(tickets):
    answer = []
    global visited
    tickets.sort()
    print(tickets)
    
    for i in tickets:
        if i[0] == "ICN" and i not in visited:
            visited.append(i)
            dfs(tickets, i[1])

    print(visited)        
            
    for i in range(len(visited)):
        if i == 0:
            answer.append(visited[i][0])
        answer.append(visited[i][1])

    return answer


'''
#Test case 1
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#return ["ICN", "JFK", "HND", "IAD"]
'''

#실패 case : 여행지가 끊어지는 경우가 발생
tickets = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
#return ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO']

print(solution(tickets))

'''
#Test case 2
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
'''