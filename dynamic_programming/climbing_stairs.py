from math import sqrt


class SolutionRecursion:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class SolutionArray:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class SolutionFibonacci:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first, second = second, third
        return second


class SolutionFibonacciFormula:
    def climbStairs(self, n: int) -> int:
        sqrt5 = sqrt(5)
        return int(1 / sqrt5 * (pow((1 + sqrt5) / 2, n) - pow((1 - sqrt5) / 2, n)))
