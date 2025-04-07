# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        max_num = max(arr)
        index_max = arr.index(max_num)

        if index_max == 0 or index_max == len(arr)-1:
            return False

        for i in range(len(arr)):
            if i < index_max:
                if arr[i] >= arr[i + 1]:
                    return False
                
            if i > index_max:
                if arr[i] >= arr[i - 1]:
                    return False
        
        return True

