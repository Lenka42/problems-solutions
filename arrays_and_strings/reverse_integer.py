class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            multiplier = -1
            x = -x
        else:
            multiplier = 1
        str_x = str(x)
        str_x = str_x[::-1]
        result = int(str_x)
        if result > 2147483647:
            return 0
        return result * multiplier
