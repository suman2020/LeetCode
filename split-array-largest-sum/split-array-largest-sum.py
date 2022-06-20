class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        #  1 2 3 | 4 | 5
        # sum = 6
        # k = 3
        
    
        
        """
        1 |  2  |  3  |  4 |  5 | 
        min_sum = 5 when n =lenght of nums
        largest_sum = 1+2+3+4+5 = 15 when m = 1
        https://www.youtube.com/watch?v=OmJuyKaGGjs
        
        
        """
        
        def canSplit(largest):
            subarray = 0
            cur_sum = 0
            for n in nums:
                cur_sum+=n
                if cur_sum > largest:
                    subarray +=1
                    cur_sum = n
                    
                    
            return subarray+1 <=m
        
        l, r = max(nums), sum(nums)
        
        res = r # largest the result could possibly be
        
        while l<=r:
            mid = (l+r)//2
            
            if canSplit(mid):
                res  = mid
                
                r = mid-1
                
            else:
                l = mid + 1
                
        return res
                
            
        
        
                    
            
        