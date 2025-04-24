# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = defaultdict(int)
        left  = 0
        maxLen = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            while seen[s[r]] > 1:
                seen[s[left]] -= 1
                
                left += 1
            maxLen = max(maxLen, r-left+1)

        return maxLen
                


