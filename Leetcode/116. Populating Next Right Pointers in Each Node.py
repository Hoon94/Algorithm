from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.left and curr.right:
                curr.left.next = curr.right

                if curr.next:
                    curr.right.next = curr.next.left

                stack.append(curr.right)
                stack.append(curr.left)
