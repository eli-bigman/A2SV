# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        # nums = nums
        self.prefix_sum = []

        size = len(nums)
        accumulator = 0
        for i in range(size):
            accumulator += nums[i]
            self.prefix_sum.append(accumulator)

        self.prefix_sum.insert(0,0)

        


    def sumRange(self, left: int, right: int) -> int:
        result = self.prefix_sum[right + 1] - self.prefix_sum[left]

        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)