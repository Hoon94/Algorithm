import heapq
import copy


def dijkstra(start_position, end_position):
    queue = []
    heapq.heappush(queue, (0, start_position))
    distance[start_position] = 0

    while queue:
        now_cost, now_node = heapq.heappop(queue)

        if distance[now_node] < now_cost:
            continue

        path[now_node].append(now_node)

        if now_node == end_position:
            break

        for next_cost, next_node in graph[now_node]:
            new_cost = distance[now_node] + next_cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node,))
                path[next_node] = copy.deepcopy(path[now_node])


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

distance = [int(1e9)] * (N + 1)
path = [[] for _ in range(N + 1)]

for _ in range(M):
    bus_start, bus_end, bus_cost = map(int, input().split())
    graph[bus_start].append((bus_cost, bus_end))

start_position, end_position = map(int, input().split())

dijkstra(start_position, end_position)

print(distance[end_position])
print(len(path[end_position]))
print(*path[end_position])
