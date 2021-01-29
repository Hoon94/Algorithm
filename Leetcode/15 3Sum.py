class Solution:
    def threeSum(self, nums: list) -> list:
        """[summary]

        Args:
            nums (List[int]): -105 <= nums[i] <= 105, 0 <= nums.length <= 3000

        Returns:
            List[List[int]]: Find all unique triplets in the array which gives the sum of zero.
        """

        result = set()

        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -num in N:
                    result.add((-num, 0, num))

        if len(z) >= 3:
            result.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    result.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    result.add(tuple(sorted([p[i], p[j], target])))

        return result
