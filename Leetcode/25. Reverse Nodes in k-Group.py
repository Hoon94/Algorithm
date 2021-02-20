# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """[summary]
            Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
            k is a positive integer and is less than or equal to the length of the linked list.
            If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

            Follow up:
            Could you solve the problem in O(1) extra memory space?
            You may not alter the values in the list's nodes, only nodes itself may be changed.

        Args:
            head (ListNode): The number of nodes in the list is in the range sz. 1 <= sz <= 5000, 0 <= Node.val <= 1000
            k (int): 1 <= k <= sz

        Returns:
            ListNode: reverse the nodes of a linked list k at a time and return its modified list.

        Result:
            Runtime: 40 ms, faster than 98.48% of Python3 online submissions for Reverse Nodes in k-Group.
            Memory Usage: 15.3 MB, less than 17.16% of Python3 online submissions for Reverse Nodes in k-Group.
        """

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
