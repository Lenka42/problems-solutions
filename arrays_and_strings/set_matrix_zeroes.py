from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        columns = set()
        rows = set()
        for r_idx, row in enumerate(matrix):
            for c_idx, cell in enumerate(row):
                if cell == 0:
                    columns.add(c_idx)
                    rows.add(r_idx)
        for r_idx, row in enumerate(matrix):
            for c_idx, cell in enumerate(row):
                if r_idx in rows or c_idx in columns:
                    matrix[r_idx][c_idx] = 0
