# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        seen = set()
        n = len(s)
        res = []
        i = j = 0

        while i < n and j < n:
            count[s[j]] -= 1
            seen.add(s[j])
            j += 1

            if all([count[x] == 0 for x in seen]):
                res.append(j - i)
                i = j
           
        
        return res



