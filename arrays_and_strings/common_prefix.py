# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
from typing import List


class SolutionPythonic:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):
            if all(chars[0] == ch for ch in chars):
                prefix += chars[0]
            else:
                break
        return prefix


class SolutionDivideAndConquer:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return self.lcp(strs, 0, len(strs) - 1)

    def lcp(self, strs: List[str], l: int, r: int) -> str:
        if l == r:
            return strs[l]
        mid = (l + r) // 2
        lcp_left = self.lcp(strs, l, mid)
        lcp_right = self.lcp(strs, mid + 1, r)
        return self.common_prefix(lcp_left, lcp_right)

    @staticmethod
    def common_prefix(left, right):
        min_length = min(len(left), len(right))
        for i in range(min_length):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_length]
