class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = 0
        merged_array = sorted(list(set(nums1 + nums2)))

        median, remain = divmod(len(merged_array), 2)
        if remain == 1: #odd
            answer = float(merged_array[median])              
        else: #even
            answer = float((merged_array[median] + merged_array[median - 1]) / 2)
            
        return answer
