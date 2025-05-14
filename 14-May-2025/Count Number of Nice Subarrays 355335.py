# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odd_count = 0
        l = 0 
        m = 0
        n = len(nums)
        for r in range(n):
            if nums[r] % 2 == 1:
                odd_count += 1
                
            while odd_count > k:
                if nums[l] % 2 == 1:
                    odd_count -= 1
                l += 1
                m = l
                
            if odd_count == k:
                while not nums[m] % 2 == 1:
                    m += 1
                res += (m - l) + 1
        return res

       