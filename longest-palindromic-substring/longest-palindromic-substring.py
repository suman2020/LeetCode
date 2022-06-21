class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # https://www.youtube.com/watch?v=6kTZYvNNyps
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length palindrom: b  a  b  a   d   --> bab or aba 
            
            l, r = i,i
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)> resLen:
                    res = s[l:r+1]
                    resLen = r -l+1
                    
                l -=1
                r +=1
            
            # even length palindrom: b   a   a  b  a ---> baab 
            
            l, r = i,i+1
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)> resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                    
                l -=1
                r +=1
            
            
        return res
            
            