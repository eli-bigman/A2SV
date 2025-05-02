# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) 
        start = 0
        end = n - 1
        max_area = float('-inf')

        while start < end:
            if height[start] < height[end]:
                h = min(height[start], height[end])
                area = h * (end - start)
                max_area = max(max_area, area)
                start += 1  
            else:
                h = min(height[start], height[end])
                area = h * (end - start)
                max_area = max(max_area, area)
                end -= 1
        

        return max_area 