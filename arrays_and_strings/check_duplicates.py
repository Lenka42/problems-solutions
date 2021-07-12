# https://leetcode.com/problems/contains-duplicate/
from typing import List


class SolutionSet:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        return False


class SolutionSort:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None
        for element in nums:
            if element == prev:
                return True
            prev = element
        return False


class SolutionLinearSearch:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i, current in enumerate(nums):
            for j in range(i):
                if nums[j] == current:
                    return True
        return False
