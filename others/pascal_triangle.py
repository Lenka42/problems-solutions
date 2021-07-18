from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        while len(result) != numRows:
            row = [1]
            for a, b in zip(result[-1], result[-1][1:]):
                row.append(a + b)
            row.append(1)
            result.append(row)
        return result
