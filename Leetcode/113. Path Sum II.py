from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [(root, [root.val])]

        while stack:
            curr, ls = stack.pop()

            if not curr.left and not curr.right and sum(ls) == ls:
                res.append(ls)

            if curr.right:
                stack.append((curr.right, ls + [curr.right.val]))

            if curr.left:
                stack.append((curr.left, ls + [curr.left.val]))

        return res
