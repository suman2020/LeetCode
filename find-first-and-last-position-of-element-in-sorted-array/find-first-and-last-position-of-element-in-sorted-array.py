class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left_index = self.binarySearch(nums,target, True)
        right_index = self.binarySearch(nums,target,False)
        # leftBias = True, rightBias = False
        
        """
        0     1    2    3    4    5
        |     |    |    |    |    |
        5     7    7    8    8    8
    ->  l          m              r
    ->             l    m         r
    -> here target is found at index m, but our first target_index might be behind the index m as well, so we move our right_pointer to the left of our middle index m
    
    ->  0     1    2    3    4    5
        |     |    |    |    |    |
        5     7    7    8    8    8
    ->             l    m         r
    ->             l
                   r,m
    ->             r,m   l end of while loop l!<=r
    
    # Similary our target is found at index m, but our second target_index might be after the index m, so we move our left_pointer to the right of our middle index and check from there
    
    ->  0     1    2    3    4    5
        |     |    |    |    |    |
        5     7    7    8    8    8
    ->             l    m         r
    ->                       l    r
    ->                       l,m  r # target found move left one step ahead
    ->                            l,r,m
        
        
        
        
        
        """
        return [left_index, right_index]
        
    def binarySearch(self,nums, target, leftBias):
        left, right = 0, len(nums) - 1
        return_index = -1
        
        while left<=right:
            middle = (left+right)//2
            if target > nums[middle]:
                left = middle+1
            elif target < nums[middle]:
                right = middle - 1
            else: # if target == nums[middle]
                return_index = middle
                if leftBias:
                    right = middle - 1
                else:
                    left = middle + 1
                
                
        return return_index
        