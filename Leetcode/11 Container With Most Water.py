class Solution:
    def maxArea(self, height: list) -> int:
        """[summary]

        Args:
            height (List[int]): i 에 대한 a[i] 값이 list로 주어진다.

        Returns:
            int: 가장 큰 넓이 값을 반환.
        """
        result = 0

        for i, i_height in enumerate(height):
            for j, j_height in enumerate(height[i+1:], i + 1):
                x = j - i
                y = min(i_height, j_height)
                if x * y >= result:
                    #print(i, i_height, j, j_height, x, y)
                    result = x * y

        return result
