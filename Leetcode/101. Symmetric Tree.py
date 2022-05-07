from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]

        while queue:
            values = [i.val if i else None for i in queue]

            if values != values[::-1]:
                return False

            queue = [child for i in queue if i for child in (i.left, i.right)]

        return True
