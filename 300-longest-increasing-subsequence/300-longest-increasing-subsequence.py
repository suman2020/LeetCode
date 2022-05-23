class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #https://www.youtube.com/watch?v=cjWnW0hdF1Y
        LIS = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            
            for j in range(i+1, len(nums)):
                
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
                    
        return max(LIS)