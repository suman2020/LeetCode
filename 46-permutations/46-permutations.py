class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        # details in notes
        # https://www.youtube.com/watch?v=s7AvT7cGdSo&t=197s
        result = []
        
        # base case:
        if (len(nums)==1):
            
            return [nums[:]] # return [nums.copy()]  
        
        for i in range(len(nums)):
            current_value = nums.pop(0)
            perms = self.permute(nums)
            print(perms)
            
            for perm in perms:
                perm.append(current_value)
                print(perm)
            print(perms)
                
            result.extend(perms) # adding multiple values
            print("result",result)
            nums.append(current_value)
            
        return result
        
        
        
        
            
            
            
            
            
            
        
        