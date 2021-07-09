# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroes_num = 0
        write_idx = 0
        for idx in range(n):
            if nums[idx] != 0:
                nums[write_idx] = nums[idx]
                write_idx += 1
        nums[write_idx:] = [0] * (n - write_idx)
