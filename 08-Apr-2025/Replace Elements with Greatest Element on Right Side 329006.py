# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_n = -1
        for i in range(1, len(arr)):
            max_n = max(max_n,arr[-i])
            if arr[-i] < max_n:
                arr[-i] = max_n

        arr.append(-1)
        arr.pop(0)
        return arr


        
