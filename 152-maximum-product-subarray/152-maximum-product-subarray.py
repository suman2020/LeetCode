class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far =  nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for value in nums[1:]:
            temp_max = max(value, max_so_far*value, min_so_far * value)
            min_so_far = min(value, max_so_far*value, min_so_far*value)
            
            max_so_far = temp_max
            
            print(max_so_far)
            result = max(result, max_so_far)
            
            
        return result
         