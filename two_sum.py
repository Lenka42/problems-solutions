from typing import List


class SolutionBrutForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            pair = target - n
            for j in range(idx + 1, len(nums)):
                if nums[j] == pair:
                    return [idx, j]


class SolutionDict:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, n in enumerate(nums):
            pair = target - n
            if pair not in d:
                d[n] = idx
            else:
                return [d[pair], idx]
