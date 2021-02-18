# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        a = []
        cur = head

        while cur:
            a.append(cur.val)
            cur = cur.next

        for i in range(0, len(a)-1, 2):
            a[i], a[i+1] = a[i+1], a[i]

        l = ListNode(-1)
        c = l

        for i in a:
            c.next = ListNode(i)
            c = c.next

        return l.next
