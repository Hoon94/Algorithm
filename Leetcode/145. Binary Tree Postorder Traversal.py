from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal, stack = [], [root]

        while stack:
            node = stack.pop()

            if node:
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return traversal[::-1]
