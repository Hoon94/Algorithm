from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l, p = 0, head

        while p:
            l += 1
            p = p.next

        return self.convert([head], 0, l - 1)

    def convert(self, head, start, end):
        if start > end:
            return None

        mid = (start + end) >> 1
        l = self.convert(head, start, mid - 1)
        root = TreeNode(head[0].val)
        root.left = l
        head[0] = head[0].next
        root.right = self.convert(head, mid + 1, end)

        return root
