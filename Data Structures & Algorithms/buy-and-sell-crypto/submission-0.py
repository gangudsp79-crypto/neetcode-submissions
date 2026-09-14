class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        max=0
        for price in prices:
            if price<min:
                min=price
            else:
                profit=price-min
                if profit>max:
                    max=profit
        return max
        
        
        