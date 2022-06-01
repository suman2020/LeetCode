class Solution:
    def canJump(self, nums: List[int]) -> bool:\
        
        
        # https://www.youtube.com/watch?v=Yan0cv2cLy8
        goal = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            
            # nums[i] >=goal - i
            # i + nums[i] >=goal
            if i+nums[i] >=goal:
                goal = i
                
        return True if goal ==0 else False 
        
        """
        
        n = len(nums)-1
        maxPos = 0
        i = 0
        while i <= maxPos:
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= n : return True
            i += 1
        
        return False
     
        i
        0   1   2   3   4   5   6
    
        2   3   1   2   0   1   4
                |
              maxP
      
            i
        0   1   2   3   4   5   6
    
        2   3   1   2   0   1   4
                        |
                      maxP
                      
                i
        0   1   2   3   4   5   6
    
        2   3   1   2   0   1   4
                        |
                      maxP
                     
                    i
        0   1   2   3   4   5   6
    
        2   3   1   2   0   1   4
                        |
                      maxP
                      
                        i
        0   1   2   3   4   5   6
    
        2   3   1   2   0   1   4
                            |
                          maxP
                          
                            i
        0   1   2   3   4   5   6
    
        2   3   1   2   0   1   4
                                |
                              maxP
      
      
      
      
        
        

        
        """