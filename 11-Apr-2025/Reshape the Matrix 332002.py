# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        flatlist = []
        result = []
        for i in range(len(mat)):
            flatlist += mat[i]
        
        for start_idx in range(r):
            result.append(flatlist[start_idx*c : start_idx * c + c])

        return result