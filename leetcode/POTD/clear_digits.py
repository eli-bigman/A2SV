'''
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".


https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10
'''


class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and i.isdigit():
                stack.pop(-1)
            else:
                stack.append(i)
        return "".join(stack)
        