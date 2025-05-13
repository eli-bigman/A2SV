# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            val = 0
            if char == "(":
                stack.append(0)

            else:
                
                while stack[-1] != 0:
                    val += stack.pop() 
                val = max(2*val, 1)
                stack.pop()
                stack.append(val)

        return sum(stack)
