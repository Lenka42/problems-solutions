from typing import List


class SolutionBrutForce:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > maxprofit:
                    maxprofit = profit
        return maxprofit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_before = prices[0]
        max_profit = 0
        for p in prices[1:]:
            profit = p - min_price_before
            if profit > max_profit:
                max_profit = profit
            if p < min_price_before:
                min_price_before = p
        return max_profit

