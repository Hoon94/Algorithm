from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.dfs(root, "")

    def dfs(self, root, path):
        if not root:
            return []
        path += str(root.val)
        if not root.left and not root.right:
            return [path]
        path += "->"
        return self.dfs(root.left, path) + self.dfs(root.right, path)
