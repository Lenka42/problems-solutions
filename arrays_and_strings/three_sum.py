from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums_dict = defaultdict(list)
        result = []
        for i, x in enumerate(nums):
            nums_dict[x].append(i)
        for i, ni in enumerate(nums):
            for j in range(i+1, n):
                nj = nums[j]
                third = - (ni + nj)
                if not [x for x in nums_dict[third] if x > j]:
                    continue
                three = sorted([ni, nj, third])
                if three in result:
                    continue
                result.append(three)
        return result


class SolutionElegant:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
