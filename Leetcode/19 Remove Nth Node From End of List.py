# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        """[summary]
            Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Args:
            head (ListNode): 1 <= nodesize <= 30, 0 <= Node.val <= 100
            n (int): 1 <= n <= nodesize

        Returns:
            ListNode: remake head

        Result:
            Runtime: 28 ms, faster than 93.43% of Python3 online submissions for Remove Nth Node From End of List.
            Memory Usage: 14.4 MB, less than 19.36% of Python3 online submissions for Remove Nth Node From End of List.
        """

        front = head
        back = head

        # advance front to nth position
        for i in range(n):
            front = front.next

        if not front:
            return head.next

        # then advance both front and back now they are nth postions apart
        # when front gets to None, back will be just before the item to be deleted
        while front.next:
            back = back.next
            front = front.next

        # delete the node
        back.next = back.next.next
        return head
