class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # converting every list elements to string cauze: string additon
        #[1,12]: 112 or 121
        for i,n in enumerate(nums):
            nums[i] = str(n)
            
        if len(nums)<2:
            return "".join(nums)
        
        x = 0
        y = 1
        
        
        def compare(x,y):
            return int(nums[x]+nums[y]) > int(nums[y]+nums[x])
        
        for x in range(len(nums)-1):
            y = x+1
        
            while x<len(nums) and y<len(nums):

                if not compare(x,y):
                    nums[x],nums[y] = nums[y],nums[x]
                
                y+=1
             
        return str(int("".join(nums)))
                
            
        