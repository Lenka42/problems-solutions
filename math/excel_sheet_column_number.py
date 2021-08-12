import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, ch in enumerate(columnTitle[::-1]):
            ch_idx = string.ascii_uppercase.index(ch) + 1
            mult = pow(26, i)
            result += ch_idx * mult
        return result
