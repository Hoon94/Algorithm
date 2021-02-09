# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """[summary]
            Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

        Args:
            l1 (ListNode): The number of nodes in both lists is in the range [0, 50], -100 <= Node.val <= 100, Both l1 and l2 are sorted in non-decreasing order.
            l2 (ListNode): The number of nodes in both lists is in the range [0, 50], -100 <= Node.val <= 100, Both l1 and l2 are sorted in non-decreasing order.

        Returns:
            ListNode: sorted list.

        Result:
            Runtime: 40 ms, faster than 50.15% of Python3 online submissions for Merge Two Sorted Lists.
            Memory Usage: 14.1 MB, less than 87.24% of Python3 online submissions for Merge Two Sorted Lists.
        """

        ret = ListNode()
        head = ret

        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next

            head = head.next

        if l1:
            head.next = l1
        else:
            head.next = l2

        return ret.next
