from collections import defaultdict, Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            anagrams_dict[ss].append(s)
        return [list(v) for k, v in anagrams_dict.items()]


