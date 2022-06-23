class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # https://www.youtube.com/watch?v=IlEsdxuD4lY
        
        prevRow = [1]*n
        
        for i in range(m-1):
            newRow = [1]*n
            
            for j in range(n-2,-1,-1):
                
                newRow[j] = newRow[j+1] + prevRow[j]
                
            prevRow = newRow
            
        return prevRow[0]