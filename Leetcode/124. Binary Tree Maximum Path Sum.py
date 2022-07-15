from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxend(node):
            if not node:
                return 0

            left = maxend(node.left)
            right = maxend(node.right)

            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)

        self.max = None
        maxend(root)

        return self.max
