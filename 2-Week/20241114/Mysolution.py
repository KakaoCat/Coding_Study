class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        max_val = prices[len(prices)-1] 
        max_profit = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i] >= max_val:
                max_val = prices[i] 
            else:
                curr_profit = max_val - prices[i] 
                if curr_profit >=max_profit:
                    max_profit = curr_profit
        return max_profit
