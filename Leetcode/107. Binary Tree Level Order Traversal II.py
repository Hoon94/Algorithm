from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque, ret = collections.deque(), []

        if root:
            deque.append(root)

        while deque:
            level, size = [], len(deque)

            for _ in range(size):
                node = deque.popleft()
                level.append(node.val)

                if node.left:
                    deque.append(node.left)

                if node.right:
                    deque.append(node.right)

            ret.append(level)

        return ret[::-1]
