class SolutionMask:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits


class SolutionBitTrick:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n != 0:
            s += 1
            n &= n - 1
        return s


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
