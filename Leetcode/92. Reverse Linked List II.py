from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left >= right:
            return head

        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head

        for _ in range(right - left):
            wtail = wtail.next

        for _ in range(left - 1):
            ohead, whead, wtail = whead, whead.next, wtail.next

        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        ohead.next, revtail.next = revhead, otail

        return dummy.next

    def reverse(self, head):
        pre, cur, tail = None, head, head

        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre, tail
