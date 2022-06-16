from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        head, curr = None, root

        while head != root:
            if curr.right == head:
                curr.right = None

            if curr.left == head:
                curr.left = None

            if curr.right:
                curr = curr.right
            elif curr.left:
                curr = curr.left
            else:
                curr.right, head, curr = head, curr, root
