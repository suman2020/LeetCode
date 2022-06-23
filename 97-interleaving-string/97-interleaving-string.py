class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        # k = i+j : i-> index of string s1, j--> index of string s2
        
        if len(s1)+len(s2) !=len(s3):
            return False
        
        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i<len(s1) and s1[i]==s3[i+j] and dfs(i+1,j):
                return True
            
            if j<len(s2) and s2[j]==s3[i+j] and dfs(i,j+1):
                return True
            
            dp[(i,j)] = False
            
            return False
        
        return dfs(0,0)
    
        """
        "aabcc" = s1
        "dbbca" = s2
        "aadbbcbcac" = s3
        
        - we check for each character in s3 and compare it with that of s1 and s2
        - for character: a in s3: we see a in s1, so we increment our index in s1
                         a in s3: we see a agian in s1, so we incremnt our index in s1
                         d in s3: we see d in s2, so we increment our index in s2
                         b in s3: we see b both in s1 and s2, so we increment both the index in s1 and s2 and return true if either one of them returns true
        
        """
            