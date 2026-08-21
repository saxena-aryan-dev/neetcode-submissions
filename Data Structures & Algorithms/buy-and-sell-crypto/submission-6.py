from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_profit=0
        for price in prices :
            buy=min(price,buy)
            profit=price-buy
            max_profit=max(profit,max_profit)
        return max_profit    