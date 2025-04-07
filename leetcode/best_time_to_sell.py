from typing import List

def maxProfit( prices: List[int]) -> int:
    min_price = min(prices)
    print(min_price)
    min_price_idx = prices.index(min_price)
    max_sell = 0
    if min_price_idx != (len(prices)- 1):
        max_price = max(prices[min_price_idx :])
        print(max_price)
        max_sell = abs(max_price - min_price)
        print(max_sell)
        
    return max_sell


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
