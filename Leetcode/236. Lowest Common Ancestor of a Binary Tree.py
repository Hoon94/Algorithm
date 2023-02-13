class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        subs = [self.lowestCommonAncestor(kid, p, q)
                for kid in (root.left, root.right)]

        return root if all(subs) else max(subs)
