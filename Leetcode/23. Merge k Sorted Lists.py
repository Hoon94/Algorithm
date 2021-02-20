from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """[summary]
            You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

        Args:
            lists (List[ListNode]): k == lists.length, 0 <= k <= 10^4, 0 <= lists[i].length <= 500,
                                    -10^4 <= lists[i][j] <= 10^4, lists[i] is sorted in ascending order.
                                    The sum of lists[i].length won't exceed 10^4.

        Returns:
            ListNode: Merge all the linked-lists into one sorted linked-list and return it.

        Result:
            Runtime: 96 ms, faster than 86.18% of Python3 online submissions for Merge k Sorted Lists.
            Memory Usage: 18.4 MB, less than 28.27% of Python3 online submissions for Merge k Sorted Lists.
        """

        res = []

        for x in lists:
            while x:
                res.append(x.val)
                x = x.next

        res = sorted(res)
        head = ListNode()
        node = head

        for x in res:
            node.next = ListNode(x)
            node = node.next

        return head.next
