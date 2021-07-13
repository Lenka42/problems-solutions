# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

class Solution:
    def read_whitespace(self, s: str) -> str:
        for i, ch in enumerate(s):
            if ch.isspace():
                continue
            else:
                return s[i:]

    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = self.read_whitespace(s)
        if not s:
            return 0

        # check multiplier
        multiplier = 1
        if s[0] == '-':
            multiplier = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = ""
        for ch in s:
            if not ch.isdigit():
                break
            result += ch

        if not result:
            return 0
        result = int(result)
        if result > 2147483647 and multiplier == 1:
            return 2147483647
        elif result > 2147483648 and multiplier == -1:
            return -2147483648
        else:
            return result * multiplier
