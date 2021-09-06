class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0
        five_div = 5
        while five_div <= n:
            total += n // five_div
            five_div *= 5
        return total
