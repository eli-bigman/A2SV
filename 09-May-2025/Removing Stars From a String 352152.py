# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for word in s:
            if stack and word == "*" :
                stack.pop()
            else:
                stack.append(word)

        return "".join(stack)