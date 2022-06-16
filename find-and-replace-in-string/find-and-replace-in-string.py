class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        """
        # not suitable for every test cases
        
        k = len(indices)
        
        diff = 0
        for i in range(k):
            
            len_curr_source = len(sources[i])
            
            current_index = indices[i] + diff
            
            if s[current_index:current_index+len_curr_source]!= sources[i]:
                continue
                
            s = s[:current_index]+targets[i]+s[current_index+len_curr_source:]
            
            diff = len(targets[i]) - len_curr_source
            
        return s
        
        
        
        """
        
        replacement = zip(sources, indices, targets)
        
        res = list(s)
        
        print(res)
        
        for source,index,target in replacement:
            
            if s[index:index+len(source)] == source:
                
                # swap the first index of result to target
                
                res[index] = target
                
                for i in range(index+1,index+len(source)):
                    res[i] = ''
                    
                    
        return ''.join(res)
    
    
        """
        s = "vmokgggqzp"
        indices = [3,5,1]
        source = ["kg","ggq","mo"]
        targets = ["s","so","bfr"]
        
        res = ['v', 'm', 'o', 'k', 'g', 'g', 'g', 'q', 'z', 'p']
                0    1    2    3    4    5    6    7    8    9
        
        res[3] = s
        res[4] = ''
        res = ['v', 'm', 'o', 's', '', 'g', 'g', 'q', 'z', 'p']
                0    1    2    3    4    5    6    7    8    9
    
        
        res[5] = so
        res[6] = ''
        res[7] = ''
        res = ['v', 'm', 'o', 's', '',  'so',  '', '', 'z', 'p']
                0    1    2    3    4    5    6    7    8    9
        
        
        res[1] = bfr
        res[2] = ''
        res = ['v', 'bfr', '', 's', '',  'so',  '', '', 'z', 'p']
                0    1     2    3    4    5    6    7    8    9
                
                
        ans = "vbfrssozp"
        
        
        
        """
    
    
    
        
        
        