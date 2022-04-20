from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return []

        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, root, path, result):
        if not root.left and not root.right:
            result.append(path + str(root.val))

        if root.left:
            self.dfs(root.left, path + str(root.val) + "->", result)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", result)
