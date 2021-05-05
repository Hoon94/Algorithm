import heapq

n = int(input())

card = list(int(input()) for _ in range(n))
heapq.heapify(card)
result = 0

while len(card) != 1:
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(card, Sum)

print(result)
