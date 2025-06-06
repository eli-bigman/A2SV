# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix  = matrix
        n = len(matrix)
        m = len(matrix[0])
        
        self.prefix_matrix= [[0] * (m +1) for _ in range(n +1)]
        
        for r in range(1, n +1):
            for c in range(1, m + 1):

                self.prefix_matrix[r][c] = self.matrix[r - 1][c - 1] + self.prefix_matrix[r][c-1] + self.prefix_matrix[r-1][c] - self.prefix_matrix[r -1][c - 1]
        



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



        result = self.prefix_matrix[row2+1 ][col2+1] - self.prefix_matrix[row2+1][col1+ 1 -1] - self.prefix_matrix[row1+1 - 1][col2+ 1] + self.prefix_matrix[row1 + 1 -1][col1 + 1 -1] 

        return result