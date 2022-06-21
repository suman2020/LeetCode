class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [7,1,5,3,6,4]
        profit = 0
        
        size = len(prices)
        
        bought = prices[0]
        
        for i in range(size):
            if bought < prices[i]:
                diff = prices[i] - bought
                profit = max(profit, diff)
            else:
                bought = prices[i]
                
        return profit
                
         
        
    
        
        
                
        
        
        
                
            
            
            
            
                
            
            
        
        
        
        