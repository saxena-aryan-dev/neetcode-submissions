class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi= 0
        buy =prices[0]
        for price in prices :
            buy =min(price,buy)
            profit = price-buy
            maxi=max(profit,maxi)
        return maxi    


        