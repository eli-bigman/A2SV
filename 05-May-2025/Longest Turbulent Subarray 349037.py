# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        ans = 1
        l, r= 0, 1
        prev = ""
        len_arr = len(arr)

        while r < len_arr:
            if arr[r-1] > arr[r] and prev != ">":
                ans = max(ans, r - l + 1)
                prev = ">"
                r += 1
            elif arr[r-1]  < arr[r] and prev != "<":
                ans = max(ans, r - l + 1)
                prev = "<"
                r += 1
            else:
                prev = ""
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
        return ans
            


