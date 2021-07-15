from collections import deque

N = int(input())
nums = list(map(int, input().split()))
stack = deque()
res = [-1] * N

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        res[stack.pop()] = nums[i]
    stack.append(i)

print(*res)
