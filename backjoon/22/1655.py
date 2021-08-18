import sys
import heapq
input = sys.stdin.readline

N = int(input())
smallheap = []
bigheap = [int(input())]
print(bigheap[0])

for i in range(2, N + 1):
    _input = int(input())
    if bigheap[0] > _input:
        heapq.heappush(smallheap, -_input)
    else:
        heapq.heappush(bigheap, _input)

    while len(bigheap) < (i // 2) + 1:
        heapq.heappush(bigheap, -heapq.heappop(smallheap))
    while len(smallheap) < i - ((i // 2) + 1):
        heapq.heappush(smallheap, -heapq.heappop(bigheap))

    print(bigheap[0])
