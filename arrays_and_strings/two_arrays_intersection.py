# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
from typing import List


class SolutionBrutForce:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n1 in nums1:
            if n1 in nums2:
                nums2.remove(n1)
                result.append(n1)
        return result


class SolutionDict:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_dict = {}
        result = []
        for n2 in nums2:
            if n2 not in nums2_dict:
                nums2_dict[n2] = 1
            else:
                nums2_dict[n2] += 1
        for n1 in nums1:
            if n1 in nums2_dict and nums2_dict[n1] > 0:
                nums2_dict[n1] -= 1
                result.append(n1)
        return result
