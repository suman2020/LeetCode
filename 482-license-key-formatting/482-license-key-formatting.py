class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.upper().replace('-','')
        size = len(s)
        
        """
        s = 'abcdefghijk' , k = 4
        len = 11, k = 4
        11%4 =3 
        ans = 'abc-defg-hijk'
        """
        # for first part:
        temp = k if size%k==0 else size%k
        
        res = s[:temp] # 'abc' --> s[0:3]
        
        while temp<size:
            res +='-'+s[temp:temp+k]
            temp +=k
            
        return res
        
        
        
        