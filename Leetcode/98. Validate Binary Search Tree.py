from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self.dfs(root, output)

        return output

    def dfs(self, root, output):
        if root is None:
            return

        for child in root.children:
            self.dfs(child, output)

        output.append(root.val)
