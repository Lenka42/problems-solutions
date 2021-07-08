# https://leetcode.com/problems/rotate-array/

from typing import List

class SolutionBrutForce:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        k %= nums_length
        for step in range(k):
            previous = nums[-1]
            for i in range(nums_length):
                nums[i], previous = previous, nums[i]


class SolutionExtraSpace:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        k %= nums_length
        temp_array = [0] * nums_length
        for i, element in enumerate(nums):
            temp_array[(i + k) % nums_length] = element
        nums[:] = temp_array


class SolutionCyclicReplacements:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_length = len(nums)
        k %= nums_length

        start = count = 0
        while count < nums_length:
            current, previous = start, nums[start]
            while True:
                next_id = (current + k) % nums_length
                nums[next_id], previous = previous, nums[next_id]
                current = next_id
                count += 1
                if start == current:
                    break
            start += 1


class SolutionReverse:
    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        nums_length = len(nums)
        k %= nums_length

        self.reverse(nums, 0, nums_length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, nums_length - 1)

