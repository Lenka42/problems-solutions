class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = dict()
        n = len(s)
        max_s = 0
        left, right = 0, 0
        while right < n:
            r = s[right]
            if r in chars:
                left = max(chars[r] + 1, left)
            max_s = max(max_s, right - left + 1)
            chars[r] = right
            right += 1
        return max_s
