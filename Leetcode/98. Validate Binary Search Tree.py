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
        self.dfs(root, 0, output)

        for i in range(len(output)):
            if i % 2 != 0:
                output[i].reverse()
            else:
                continue

        return output

    def dfs(self, root, level, output):
        if root is None:
            return

        if len(output) < level + 1:
            output.append([])

        output[level].append(root.val)
        self.dfs(root.left, level + 1, output)
        self.dfs(root.right, level + 1, output)
