class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # refer to notes 
        dp = [0] * (target+1)
        
        dp[0]=1
        
        for current_sum in range(target+1):
            for num in nums:
                if current_sum - num >=0:
                    dp[current_sum] +=dp[current_sum-num]
                    
                    
        return dp[-1]
    
        """
        nums=[1,2,3]
        target = 4
        
        current_sum - num >=0
        
            0-1 X    0-2 X    0-3 X    
            1-1      1-2 X    1-3 X
            2-1      2-2      2-3 X
            3-1      3-2      3-3
            4-1      4-2      4-3
            
            0       1       2       3       4       
    dp[i]   1       1       2       4       7       
    
        
        
        """
        