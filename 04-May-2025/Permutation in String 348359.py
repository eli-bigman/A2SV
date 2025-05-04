# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s2 = len(s2)
        len_s1 = len(s1)
        res = []

        if len_s2 < len_s1:
            return False
        
        for i in range(len_s1):
            res.append(s2[i])

            if Counter(res) == Counter(s1):
                print(res)
                print(s1)
                return True
        #slide throught s2 with window of len s1
        for j in range(len_s1, len_s2):
            res.append(s2[j])
            res.pop(0)
            if Counter(res) == Counter(s1):
                print(res)
                print(s1)
                return True

        return False







