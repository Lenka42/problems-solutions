# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
from typing import List


# brut force recursion approach
# Time complexity : O(n^n), space complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.calculate(prices, 0)

    def calculate(self, prices: List[int], s: int) -> int:
        if s >= len(prices):
            return 0
        max_ = 0
        for start in range(s, len(prices)):
            max_profit = 0
            for i in range(start + 1, len(prices)):
                if prices[i] > prices[start]:
                    profit = self.calculate(prices, i + 1) + prices[i] - prices[start]
                    if profit > max_profit:
                        max_profit = profit
            if max_profit > max_:
                max_ = max_profit
        return max_


# peak-valley approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit

