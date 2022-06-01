class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        
        # 1 5 8 4 7 6 5 3 1
        # find the position of element that requires swap.
        # here 7 6 5 4 3 1 are in descending order and this order is broken when 4 is reached
        
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
            
        # thie while loop will postion the index i to position of element 7 in this case:
        # so we have our k = i-1 one step below
        k = i-1
           
        # found the elements in desending order
        if i==0:
            nums.reverse()
            return
        
        # we have to find the element that is slightly greater than the element at postion k
        # in our case element 5 is greater than our element at index k 
        j = len(nums) -1
        while nums[j] <=nums[k]:
            j-=1
            
        nums[k],nums[j] = nums[j],nums[k]
        
        # so making a swap of element 4 and element 5
        
        # swap elements from k+1 to the end of our list
        l, r = k+1, len(nums) - 1
        
        # the elements are automatically sorted in descending order, so we just gonna have to swap last and first index
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1
            
        # 5 4 3 2 1 --> no larger permutatation than this, so we reverse the list
        
        """
        
        

        """
        