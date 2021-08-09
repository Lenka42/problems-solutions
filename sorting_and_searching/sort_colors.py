from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0: 0, 1: 0, 2: 0}
        for n in nums:
            d[n] += 1
        i = 0
        while i < d[0]:
            nums[i] = 0
            i += 1
        j = i
        while j < d[1] + d[0]:
            nums[j] = 1
            j += 1
        k = j
        while k < len(nums):
            nums[k] = 2
            k += 1


class SolutionDutchFlag:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
