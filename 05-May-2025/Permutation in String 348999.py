# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)

        window = len(s1)
        i = 0

        while i <= len(s2) - window:
            if counter_s1 == Counter(s2[i:i+window]):
                return True
            i += 1

        return False








