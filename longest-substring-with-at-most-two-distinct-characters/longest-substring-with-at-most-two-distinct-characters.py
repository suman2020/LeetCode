class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        temp_set = set()
        
        next_start, left, right = 0,0,0
        
        count = 1
        
        while right < len(s):
             
            if s[right] not in temp_set:
                
                if len(temp_set)==2:
                    left = next_start
                    temp_set = set()
                    temp_set.add(s[next_start])
                    temp_set.add(s[right])
                    
                next_start = right
                temp_set.add(s[right])
                
            if len(temp_set)==2:
                if s[next_start]!=s[right]:
                    next_start = right
                
            count = max(count, right-left+1)
                
            right+=1
            
        return count
        