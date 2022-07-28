from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        deque, res = collections.deque(), 0

        if root:
            deque.append(root)

        while deque:
            node = deque.popleft()

            if not node.left and not node.right:
                res += node.val

            if node.left:
                node.left.val += node.val * 10
                deque.append(node.left)

            if node.right:
                node.right.val += node.val * 10
                deque.append(node.right)

        return res
