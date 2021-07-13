from collections import Counter, defaultdict


class SolutionTwoDicts:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        return s_dict == t_dict


class SolutionOneDict:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        for char in t:
            char_dict[char] -= 1
        for char, counter in char_dict.items():
            if counter != 0:
                return False
        return True


class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


class SolutionSorting:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)

        return s == t
