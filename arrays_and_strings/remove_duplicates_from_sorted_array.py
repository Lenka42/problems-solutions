# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

from typing import List


# my solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_element = None
        i = 0
        while True:
            if i >= len(nums):
                break
            element = nums[i]
            if element == last_element:
                nums.pop(i)
            else:
                last_element = element
                i += 1
        return len(nums)


# alternative solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
