class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        
        """

        1   2   4   10  12  : lower = -1        upper = 15
        
        prev = -1-1 = -2
        curr = 1
        
        prev+1 <= curr-1
            :   -2+1 <=1-1 (true)
        
        result: ["-1 -> 0"]
        
        prev = 1
        curr = 2
        
        prev+1 <= curr-1
            :   1+1 <=2-1 (false)
        
        result: ["-1 -> 0"]
        
        
        prev = 2
        curr = 4
        
        prev+1 <= curr-1
            :   2+1 <=4-1 (true)
        
        result: ["-1 -> 0", "3"]

        
        
        
        """
        
        result = []
        prev = lower - 1
        
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)
        
        for i in range(len(nums)+1):
            current = nums[i] if i <len(nums) else upper+1
            
            if prev + 1 <=current-1:
                result.append(formatRange(prev+1,current-1))
                
            prev = current
            
            
        return result
        
        
        