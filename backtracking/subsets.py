from typing import List


# cascading
class SolutionCascading:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result


# backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, curr):
            if len(curr) == k:
                result.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        result = []
        n = len(nums)

        for k in range(n + 1):
            backtrack(0, [])
        return result
