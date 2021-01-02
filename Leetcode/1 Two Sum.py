class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            value = target - nums[i]
            if value in nums and i != nums.index(value):
                return [i, nums.index(value)]