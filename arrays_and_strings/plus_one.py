# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
from typing import List


class SolutionToStr:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(map(str, digits))
        num = int(num_str)
        num += 1
        return [int(char) for char in str(num)]


class SolutionLikeInSchool:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
                else:
                    digits[i] = 0
                    continue
            else:
                digits[i] = digits[i] + 1
                return digits


