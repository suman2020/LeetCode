class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
#         max_so_far =  nums[0]
#         min_so_far = nums[0]
#         result = max_so_far
        
#         for value in nums[1:]:
#             temp_max = max(value, max_so_far*value, min_so_far * value)
#             min_so_far = min(value, max_so_far*value, min_so_far*value)
            
#             max_so_far = temp_max
            
#             print(max_so_far)
#             result = max(result, max_so_far)
            
            
#         return result

            # 2,-5 -2,-4,3
            ans = nums[0]
            current = 1
            # left to right pass. Captures all potential subarrays containing first odd n negative numbers
            for i in nums:
                current*=i
                ans = max(ans, current)
                # zero is a delimiter, restart at 1. This is optimal since zero multiplied on is still zero.
                if current == 0:
                    current = 1
            current = 1
            print(ans)
            # right to left pass capturing all potential subarrays containing last odd n negative numbers
            for i in reversed(nums):
                current*=i
                ans = max(ans, current)
                if current == 0:
                    current = 1
            return ans
         