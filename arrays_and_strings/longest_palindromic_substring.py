class Solution:
    def expand_around_center(self, s: str, left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 0
        max_str = ""
        for i in range(len(s)):
            l1, r1 = self.expand_around_center(s, i, i)
            l2, r2 = self.expand_around_center(s, i, i+1)
            if r2 - l2 + 1 > max_len and r2 - l2 > r1 - l1:
                max_len = r2 - l2 + 1
                max_str = s[l2:r2+1]
            elif r1 - l1 + 1 > max_len and r1 - l1 >= r2 - l2:
                max_len = r1 - l1 + 1
                max_str = s[l1:r1+1]
        return max_str


