from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_2_hold, dp_2_not_hold = -float('inf'), 0
        dp_1_hold, dp_1_not_hold = -float('inf'), 0

        for stock_price in prices:
            dp_2_not_hold = max(dp_2_not_hold, dp_2_hold + stock_price)
            dp_2_hold = max(dp_2_hold, dp_1_not_hold - stock_price)
            dp_1_not_hold = max(dp_1_not_hold, dp_1_hold + stock_price)
            dp_1_hold = max(dp_1_hold, 0 - stock_price)

        return dp_2_not_hold
