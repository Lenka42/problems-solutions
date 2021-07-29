import random
from copy import deepcopy
from typing import List


class SolutionNaive:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.init_nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.init_nums[:]
        return self.init_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


class SolutionLessNaive:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.init_nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.init_nums[:]
        return self.init_nums

    def shuffle(self) -> List[int]:
        aux = self.nums[:]
        for i in range(len(self.nums)):
            remove_idx = random.randrange(len(aux))
            self.nums[i] = aux.pop(remove_idx)
        return self.nums


# Fisher-Yates Algorithm
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.init_nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.init_nums[:]
        return self.init_nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[swap_idx], self.nums[i] = self.nums[i], self.nums[swap_idx]
        return self.nums
