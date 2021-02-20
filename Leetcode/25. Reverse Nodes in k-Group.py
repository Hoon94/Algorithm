# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head

        # count number of elements
        cur = head
        n_elem = 0
        while cur is not None:
            n_elem += 1
            cur = cur.next

        if n_elem == 1:
            return head

        # determine number of swaps
        n_swaps = n_elem // k

        dummy = ListNode(val=0, next=head)
        prev = dummy
        cur = head
        one_before_interval = dummy

        for i in range(n_swaps):
            first_in_interval = cur

            for j in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # rig the first node from the original interval
            # (i.e the last node in the current reversed interval)
            # to the first following node (in interval or not)
            # this gets overturned if more intervals will be reversed
            first_in_interval.next = cur

            # rig the last node from the previous interval to the
            # NEW first node from the current reversed interval
            one_before_interval.next = prev

            one_before_interval = first_in_interval

        return dummy.next
