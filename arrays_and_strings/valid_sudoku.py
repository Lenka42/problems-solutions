# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

from typing import List

NINE_DIGITS_SET = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Solution:
    def is_valid_set_of_numbers(self, row: List[str]) -> bool:
        row_set = set(row)
        if len(row_set) != len(row):
            return False
        if row_set.issubset(NINE_DIGITS_SET):
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell == ".":
                    continue
                try:
                    cell = int(cell)
                except TypeError:
                    return False
                square_idx = (row_idx // 3) * 3 + col_idx // 3
                rows[row_idx].append(cell)
                columns[col_idx].append(cell)
                squares[square_idx].append(cell)
        for row in rows:
            if not self.is_valid_set_of_numbers(row):
                print('Invalid row', row)
                return False
        for column in columns:
            if not self.is_valid_set_of_numbers(column):
                print('Invalid column', column)
                return False
        for square in squares:
            if not self.is_valid_set_of_numbers(square):
                print('Invalid square', square)
                return False
        return True

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                y = i // 3
                x = j // 3
                num = board[i][j]
                if (num in rows[i]) or (num in columns[j]) or (num in squares[x][y]):
                    return False
                else:
                    rows[i].add(num)
                    columns[j].add(num)
                    squares[x][y].add(num)
        return True
