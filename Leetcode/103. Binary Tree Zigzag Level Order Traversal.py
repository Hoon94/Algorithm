import imp
from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque([root])
        even_level = False

        while queue:
            n = len(queue)
            level = collections.deque()

            for _ in range(n):
                node = queue.popleft()

                if even_level:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(list(level))
            even_level = not even_level

        return res
