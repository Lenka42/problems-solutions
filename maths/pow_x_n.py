class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        pow_half, reminder = divmod(n, 2)
        lower = self.myPow(x, pow_half)
        if reminder:
            return lower * lower * x
        else:
            return lower * lower
