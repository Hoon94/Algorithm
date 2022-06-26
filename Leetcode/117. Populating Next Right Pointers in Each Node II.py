# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tail = dummy = Node(0)

        while node:
            tail.next = node.left

            if tail.next:
                tail = tail.next

            tail.next = node.right

            if tail.next:
                tail = tail.next

            node = node.next

            if not node:
                tail = dummy
                node = dummy.next
