# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ret = head
        length = head
        l = 1

        while length.next:
            l += 1
            length = length.next

        target = l - n
        for i in range(target - 1):
            ret = ret.next

        ret.next = ret.next.next

        return head
