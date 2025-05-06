# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'-','+','/','*'}

        for i in range(len(tokens)):
            
            if tokens[i] in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                result = operate(a,b,tokens[i])
                print(a,b,result)
                stack.append(result)
            else:
                stack.append(tokens[i])


        return int(stack.pop()) 




def operate(a,b,operand):
    if operand == "+":
        return int(a + b)
    elif operand == "/":
        return int(a / b)
    elif operand == "-":
        return int(a - b)
    elif operand == "*":
        return int(a * b)
