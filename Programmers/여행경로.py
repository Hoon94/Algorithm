def solution(tickets):

    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]

    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    return path[::-1]

#Test case 1
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#return ["ICN", "JFK", "HND", "IAD"]

print(solution(tickets))

'''
#Test case 2
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
'''