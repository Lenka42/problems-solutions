from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            n, mod = divmod(n, 3)
            if mod != 0:
                return False
        return n == 1


class SolutionMath:
    def isPowerOfThree(self, n: int) -> bool:
        return log(n, 3) % 1 == 0
