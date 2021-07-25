from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = n * (n + 1) // 2
        for i in nums:
            sum_n -= i
        return sum_n


class SolutionXOR:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= (i ^ n)
        return missing
