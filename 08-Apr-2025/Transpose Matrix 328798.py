# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        no_row = len(matrix)
        no_col = len(matrix[0])
        transpose = [[0 for _ in range(no_row)] for _ in range(no_col)]
        for row in range(no_row):
            for col in range(no_col):
                transpose[col][row] = matrix[row][col]
        return transpose

                