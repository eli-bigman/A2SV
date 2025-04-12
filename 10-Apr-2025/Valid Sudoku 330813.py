# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows , cols = len(board), len(board[0])

        #verify each column
        
        for i in range(rows):
            seen_cols = set()

            for j in range(cols):
                
                if board[j][i] == ".":
                    continue

                if board[j][i] in seen_cols:
                    return False
                seen_cols.add(board[j][i])
                
                

        #verify each row
        for i in range(rows):
            seen_cols = set()
        
            for j in range(cols):
                
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen_cols:
                    return False
                
                seen_cols.add(board[i][j])

        #verify each 3x3
        hashmap = defaultdict(set)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in hashmap[(i//3, j//3)]):
                    return False
                hashmap[(i//3, j//3)].add(board[i][j])

        return True