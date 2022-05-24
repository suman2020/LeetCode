class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) %2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        
        for i in range(len(nums)):
            temp_dp = set()
            for value in dp:
                temp_dp.add(value+nums[i])
                temp_dp.add(value)
                
                if target in temp_dp:
                    return True
                
            dp = temp_dp
                
        return False
        
        """
        nums = [1,5,11,2,7]    target = sum//2 = 13
        
        set = {0}
        
        First iteration: value-->1 
            set = {0,1}
        Second iteration: value-->5
            set = {0,1,5,6}
        Third iteration: value-->11 
            set = {0,1,5,6,11,12,16,17}
        Fourth iteration: value-->2
            set = {0,1,5,6,11,12,16,17,2,3,7,9,13,14,18,19} //found target 11
        Fifth iteration: value-->1 
            set = {0,1}
        
            
        
            
        
        """