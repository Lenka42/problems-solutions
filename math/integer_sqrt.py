class SolutionBinarySearch:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1


class SolutionNewton:
    def mySqrt(self, x: int) -> int:
        prev = x
        curr = x / 2
        precision = 0.1
        while abs(prev - curr) > precision:
            prev = curr
            curr = (1 / 2) * (curr + x / curr)

        return int(curr)
