from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        worklist = deque([root])
        num_node_level = 1
        levels = 0

        while worklist:
            node = worklist.popleft()

            if node.left:
                worklist.append(node.left)

            if node.right:
                worklist.append(node.right)

            num_node_level -= 1

            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)

        return levels
