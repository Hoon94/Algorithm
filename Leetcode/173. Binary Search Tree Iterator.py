from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.pushAll(root)

    def next(self) -> int:
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)

        return tmpNode.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
