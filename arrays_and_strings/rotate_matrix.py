from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2 + 1):
            first = layer
            last = n - 1 - layer

            for i in range(first, last + 1):
                offset = n - 1 - i

                # save top
                top = matrix[first][i]

                # left => top
                matrix[first][i] = matrix[offset][first]

                # bottom => left
                matrix[offset][first] = matrix[last][offset]

                # right => bottom
                matrix[last][offset] = matrix[i][last]

                # top => right
                matrix[i][last] = top
