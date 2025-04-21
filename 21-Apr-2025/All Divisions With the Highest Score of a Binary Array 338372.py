# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score_dict = defaultdict(list)
        zero_count = 0
        total_ones = nums.count(1)
        
        # if total_ones:
        score_dict[total_ones].append(0)

        for idx in range(0, len(nums)):
            if nums[idx] == 0:
                zero_count += 1
                score = zero_count + total_ones
                score_dict[score].append(idx+1)
            else:
                total_ones -= 1
                score = zero_count + total_ones
                score_dict[score].append(idx+1)

        return score_dict[max(score_dict)] 




            

            
