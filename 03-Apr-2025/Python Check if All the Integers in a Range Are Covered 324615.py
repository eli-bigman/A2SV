# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen_values = set()

        for item in ranges:
            start = item[0]
            stop = item[1]

            for num in range(start, stop+1):
                seen_values.add(num)
        
        for number in range(left, right+1):
            if number not in seen_values:
                return False
    
        return True