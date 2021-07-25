from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]  # dp[i] means maximum subarray ending with nums[i]
        s_max = dp[0]
        for i in range(1, n):
            dp.append(nums[i] + (dp[i-1] if dp[i-1] > 0 else 0))
            s_max = max(dp[i], s_max)
        return s_max


class SolutionDivideAndConquer:
    def divide_and_conquer(self, nums, i, j):
        if i == j-1:
            return nums[i], nums[i], nums[i], nums[i]

        # we will compute :
        # a which is max contiguous sum in nums[i:j] including the first value
        # m which is max contiguous sum in nums[i:j] anywhere
        # b which is max contiguous sum in nums[i:j] including the last value
        # s which is the sum of all values in nums[i:j]

        # compute middle index to divide array in two halves
        i_mid = i + (j - i) // 2

        # compute a, m, b, s for left half
        a1, m1, b1, s1 = self.divide_and_conquer(nums, i, i_mid)

        # compute a, m, b, s for right half
        a2, m2, b2, s2 = self.divide_and_conquer(nums, i_mid, j)

        a = max(a1, s1 + a2)
        b = max(b2, s2 + b1)
        m = max(m1, m2, b1 + a2)
        s = s1 + s2

        return a, m, b, s

    def maxSubArray(self, nums: List[int]) -> int:
        _, m, _, _ = self.divide_and_conquer(nums, 0, len(nums))
        return m
