class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        n = len(s)
        i = n - 1
        while i >= 0:
            curr = s[i]
            curr_num = symbols[curr]
            if i == 0:
                result += curr_num
                return result
            prev = s[i-1]
            prev_num = symbols[prev]
            if prev_num < curr_num:
                result += curr_num - prev_num
                i -= 2
                continue
            result += curr_num
            i -= 1
        return result
