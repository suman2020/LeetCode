class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        index = 0
        size = len(nums)
        if size==1:
            return nums[0]
        
        max_sum = current_sum = nums[0]
        
        for element in nums[1:]:
            
            # if the current_sum is negative, then we start over
            # making the current_sum equal to the positive number
            """
            1 -2 2
            1st iteration: currentsum = 1
            2nd iteration: currentsum = -2, 1 -2 = -1
            3rd iteration: currentsum = 2,-1,= 2
            """
            current_sum = max(element, current_sum + element)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
            
            