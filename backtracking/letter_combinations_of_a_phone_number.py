from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters_dict = {
            "1": [],
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = [''] if digits else []
        for d in digits:
            combinations = [p + q for p in combinations for q in num_to_letters_dict[d]]
        return combinations


