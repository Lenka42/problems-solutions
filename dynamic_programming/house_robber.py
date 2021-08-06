from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        memo = [0, nums[0]]
        for i in range(1, n):
            memo.append(max(memo[i-1] + nums[i], memo[i]))
        return memo[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        prev1 = 0
        prev2 = nums[0]
        for i in range(1, n):
            curr = max(prev1 + nums[i], prev2)
            prev1, prev2 = prev2, curr
        return prev2
