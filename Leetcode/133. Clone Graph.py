from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        m, visited, stack = dict(), set(), deque([node])

        while stack:
            n = stack.pop()

            if n in visited:
                continue

            visited.add(n)

            if n not in m:
                m[n] = Node(n.val)

            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)

                m[n].neighbors.append(m[neigh])
                stack.append(neigh)

        return m[node]
