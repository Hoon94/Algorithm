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
        stack = [root]

        while stack:
            temp = stack.pop()

            if temp:
                output.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)

        return output
