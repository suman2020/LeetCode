class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        result = 0
        n = len(columnTitle)
        
        for i in range(n):
            result = result * 26
            result += (ord(columnTitle[i])-ord('A')+1)
            
        return result
        
        """
        A = 1
        AB  = 1*26 + 2 = 28
        ABC = 28*26 + 3 = 731
        
        """
        