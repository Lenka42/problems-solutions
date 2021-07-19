# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version: int) -> bool:
    return True


# binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        good = 0
        bad = n
        curr = n // 2
        while True:
            is_bad = isBadVersion(curr)
            if is_bad:
                bad = curr
            else:
                good = curr
            if bad == good + 1:
                return bad
            curr = (bad - good) // 2 + good
