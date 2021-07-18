class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        return bin(result).count('1')
