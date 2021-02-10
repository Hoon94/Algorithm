class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = set()
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                low = j + 1
                high = n - 1

                while low < high:
                    guess = (nums[i], nums[j], nums[low], nums[high])
                    guess_sum = sum(guess)

                    if target == guess_sum:
                        ret.add(guess)

                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1

                    elif target < guess_sum:
                        high -= 1
                    else:
                        low += 1

        return [list(r) for r in ret]
