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
        ls = []

        while head:
            ls.append(head.val)
            head = head.next

        return self.helper(ls, 0, len(ls) - 1)

    def helper(self, ls, start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(ls[start])

        mid = (start + end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid - 1)
        root.right = self.helper(ls, mid + 1, end)

        return root
