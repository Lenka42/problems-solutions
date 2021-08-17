class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (divisor < 0) is (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            curr_divisor = divisor
            num_divisors = 1
            while dividend >= curr_divisor:
                dividend -= curr_divisor
                result += num_divisors

                curr_divisor = curr_divisor << 1
                num_divisors = num_divisors << 1
        result = result if positive else - result
        return min(max(-2147483648, result), 2147483647)
