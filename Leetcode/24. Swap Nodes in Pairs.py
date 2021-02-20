from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """[summary]
            Given a linked list, swap every two adjacent nodes and return its head.

        Args:
            head (ListNode): 0 <= Node.val <= 100, The number of nodes in the list is in the range [0, 100].

        Returns:
            ListNode: head

        Result:
            Runtime: 20 ms, faster than 99.23% of Python3 online submissions for Swap Nodes in Pairs.
            Memory Usage: 14.2 MB, less than 80.37% of Python3 online submissions for Swap Nodes in Pairs.
        """

        if not head:
            return head

        l1 = head
        l2 = head.next

        while l2:
            l1.val, l2.val = l2.val, l1.val
            if not l2.next:
                break
            l1 = l1.next.next
            l2 = l2.next.next

        return head
