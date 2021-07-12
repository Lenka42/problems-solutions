import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        s = ''.join(s)
        n = len(s)

        left = 0
        right = n - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class SolutionRegexp:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", '', s.lower())
        return s == ''.join(reversed(s))
