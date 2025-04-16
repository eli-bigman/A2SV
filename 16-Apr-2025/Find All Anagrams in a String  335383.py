# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []

        p_counter = Counter(p)

        for end in range(len(s)):
            if Counter(s[end:end+len(p)]) == p_counter:
                output.append(end)

        return output

