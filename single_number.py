# https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n_pairs = len(nums) // 2
        if n_pairs == 1:
            return nums[0]
        for i in range(n_pairs):
            first, second = nums[2 * i], nums[2 * i + 1]
            if first != second:
                return first
        return nums[-1]


class SolutionMath:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


class SolutionBitXOR:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
