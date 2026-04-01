class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 0
        
        while buy <= sell and sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            sell += 1
        
        return max_profit