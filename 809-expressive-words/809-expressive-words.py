class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        ans = 0
        
    
        def getLength(str_, index):
            
            count = 1
            for i in range(index,len(str_)-1):
                if str_[i]== str_[i+1]:
                    count+=1
                    
                else:
                    break
                    
            return count
                
        
        def check(word):
            
            i,j=0,0 # i-> pointer for string s , j --> pointer for string word
            
            while i<len(s) and j < len(word):
                
            
                ch_s = s[i] # current character in string s at index i
                ch_w = word[j] # current character in string word at index j
                
                
                if ch_s !=ch_w:
                    return False
                
                
                else:
                    len1 = getLength(s,i) # get no of repeated consecutive character in string s
                    len2 = getLength(word,j) # get no of repeatd consecutive character in string word
                    
                    if len1==len2:
                        i = i+len1
                        j = j+len2
                        
                        
                    elif len2 < len1 and len1 >=3:
                        
                        i = i+len1
                        j = j+len2
                        
                    else: # if len2 > len1 or (len2 < len1 and len1 < 3)
                        return False
                          
            return i==len(s) and j==len(word)  
            
        
        for word in words:
            if check(word):
                ans+=1
                
        return ans
        