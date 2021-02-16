class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
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
