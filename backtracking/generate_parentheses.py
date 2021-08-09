from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        ln = 2 * n

        def backtrack(s: List[str], left=0, right=0):
            if len(s) == ln:
                result.append(''.join(s))
                return
            if left < n:
                s.append("(")
                backtrack(s, left+1, right)
                s.pop()
            if right < left:
                s.append(")")
                backtrack(s, left, right+1)
                s.pop()
        backtrack([])
        return result
