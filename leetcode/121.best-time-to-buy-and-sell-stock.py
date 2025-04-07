#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = min(prices)
        min_price_idx = prices.index(min_price)
        max_sell = 0
        if min_price_idx != (len(prices)- 1):
            max_price = max(prices[min_price_idx :])
            max_sell = abs(max_price - max_sell)
            
        return max_sell

        
        
# @lc code=end

