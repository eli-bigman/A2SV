# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]

        i = 0
        while len(arr) > 1:
            i += k-1
            i = i % len(arr) 
            arr.pop(i)
             
        return arr.pop()


        

                
        



        