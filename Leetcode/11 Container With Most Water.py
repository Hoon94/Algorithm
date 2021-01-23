class Solution:
    def maxArea(self, height: list) -> int:
        """[summary]

        Args:
            height (List[int]): i 에 대한 a[i] 값이 list로 주어진다.

        Returns:
            int: 가장 큰 넓이 값을 반환.
        """

        result = 0
        start = 0
        end = len(height) - 1

        while start < end:
            if height[start] > height[end]:
                area = (end - start) * height[end]
                end -= 1
            else:
                area = (end - start) * height[start]
                start += 1

            result = max(result, area)

        return result
