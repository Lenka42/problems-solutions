class SolutionCheat:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        h_len = len(haystack)
        if h_len < n_len:
            return -1
        if n_len == 0:
            return 0

        for i in range(0, h_len - n_len + 1):
            for j in range(n_len):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP algorithm must be here
        pass
