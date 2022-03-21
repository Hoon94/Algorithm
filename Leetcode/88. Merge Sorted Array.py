from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        writeIndex = m + n - 1
        m, n = m - 1, n - 1

        while n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[writeIndex] = nums1[m]
                m -= 1
            else:
                nums1[writeIndex] = nums2[n]
                n -= 1

            writeIndex -= 1

        if n > -1:
            nums1[0:n + 1] = nums2[0:n + 1]
