from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, sl = head, ListNode()

        while p:
            q = sl

            while q.next and q.next.val < p.val:
                q = q.next

            p.next, q.next, p, q = q.next, p, p.next, q.next

        return sl.next
