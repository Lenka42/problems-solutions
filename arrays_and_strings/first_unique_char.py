from collections import defaultdict


class SolutionBrutForce:
    def firstUniqChar(self, s: str) -> int:
        for idx, char in enumerate(s):
            is_unique = True
            for idx2 in range(len(s)):
                if idx == idx2:
                    continue
                if s[idx2] == char:
                    is_unique = False
                    break
            if is_unique:
                return idx
        return -1


class SolutionDict:
    def firstUniqChar(self, s: str) -> int:
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        for idx, char in enumerate(s):
            if s_dict[char] == 1:
                return idx
        return -1
