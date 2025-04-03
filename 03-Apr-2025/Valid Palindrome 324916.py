# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [i.lower() for i in s if i.isalnum()]
        print(string)

        left = 0
        right = len(string) - 1
        
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
        