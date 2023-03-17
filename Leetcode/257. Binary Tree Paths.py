from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack, ret = [(root, "")], []

        while stack:
            node, path = stack.pop()

            if node:
                if not node.left and not node.right:
                    ret.append(path+str(node.val))

                s = path + str(node.val) + "->"
                stack.append((node.right, s))
                stack.append((node.left, s))

        return ret
