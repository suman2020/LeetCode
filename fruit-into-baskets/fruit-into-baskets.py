class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        # sliding window technique
        
        if fruits is None or len(fruits)==0:
            return 0
        
        temp_dict = {} 
        left = 0 
        result = 0
        
        for j,v in enumerate(fruits):
            temp_dict[v] = temp_dict.get(v,0)+1
            
            while len(temp_dict)>2:
                temp_dict[fruits[left]]-=1
                
                if temp_dict[fruits[left]]==0:
                    del temp_dict[fruits[left]]
                
                left+=1
                
                
            result = max(result,j-left+1)
            
        
        return result
                
        