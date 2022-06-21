class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # edge case: 
        dp = [amount + 1] * (amount +1)
        
        dp[0] = 0
        
        for a in range(1,amount+1):
            for c in coins:
                if a-c >=0:  
                    dp[a] = min(dp[a], 1+dp[a-c])
                    
        return dp[amount] if dp[amount] !=amount+1 else -1
    
        # Time: 0(amount * no_of_coints)
        # Space: 0(amount)
                    
            
        """
        amount = 7, coins = [1,3,4,5]
        dp = [8,8,8,8,8,8,8,8] --> no of coins used eg: dp[0] = 8, dp[1] = 8 coins used and so on i.e to get 1 amount 8 couns are used(just a starting case)
        
        dp[0] = 0
        
        for a = 1:
            c in [1,3,4,5]
                (c=1)
                    a-c = 1-1 >=0:
                     dp[1]--> no of coins to get amount 1 == min(dp[1], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[1] = 1+0 = 1
                (c=3)
                    a-c = 1-3 = -2 !>=0 -- no execution
                    
        So dp[1] = 1
        
        
       for a = 2:
            c in [1,3,4,5]
                (c=1)
                    a-c = 2-1 >=0:
                     dp[2]--> no of coins to get amount 2 == min(dp[2], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[2] = 1+dp[2-1] = 1 + dp[1] = 2
                (c=3)
                    a-c = 2-3 = -1 !>=0 -- no execution 
        so dp[2] = 2
        
        
        for a = 3:
            c in [1,3,4,5]
                (c=1)
                    a-c = 3-1 >=0:
                     dp[3]--> no of coins to get amount 3 == min(dp[3], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[3] = 1+dp[3-1] = 1 + dp[2] = 3
                (c=3)
                    a-c = 3-3 >=0:
                     dp[3]--> no of coins to get amount 1 == min(dp[3], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[3] = min(dp[3],1+dp[3-3]) = min(3, 1+ dp[0]) --> 1
                (c=4)
                    a-c = 3-4 = -1 !>=0 -- no execution   
                    
        so dp[3] = 1
        
        for a = 4:
            c in [1,3,4,5]
                (c=1)
                    a-c = 4-1 >=0:
                     dp[4]--> no of coins to get amount 4 == min(dp[4], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[3] = 1+dp[4-1] = 1 + dp[3] = 2
                (c=3)
                    a-c = 4-3 >=0:
                     dp[3]--> no of coins to get amount 1 == min(dp[3], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[3] = min(dp[4],1+dp[4-3]) = min(2, 1+ dp[1]) --> 2
                (c=4)
                    a-c = 4-4 >=0:
                     dp[4]--> no of coins to get amount 1 == min(dp[4], 1 + dp[a-c]) --> used 1 + dp[a-c] cause 1 represents that one coin is used in this iteration
                     dp[4] = min(dp[4],1+dp[4-4]) = min(2, 1+ dp[0]) --> 1   
                     
                (c=5)
                    a-c = 4-5 = -1 !>=0 -- no execution   
                    
        so dp[4] = 1
        
    
                  
        
        """
                
        
        