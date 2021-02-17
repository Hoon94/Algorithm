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
            Runtime: 116 ms, faster than 51.23% of Python3 online submissions for Merge k Sorted Lists.
            Memory Usage: 23.7 MB, less than 5.03% of Python3 online submissions for Merge k Sorted Lists.
        """

        def listVals(node):
            while node:
                yield node.val
                node = node.next

        def merged():
            heap = []
            iters = list(map(listVals, lists))
            for i, it in enumerate(iters):
                if (v := next(it, None)) is not None:
                    heapq.heappush(heap, (v, i))
            while heap:
                v, i = heapq.heappop(heap)
                yield v
                if (v := next(iters[i], None)) is not None:
                    heapq.heappush(heap, (v, i))

        dummy = ListNode()
        p = dummy
        for val in merged():
            node = ListNode(val)
            p.next = node
            p = p.next
        return dummy.next
