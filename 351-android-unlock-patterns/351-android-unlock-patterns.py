class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # https://leetcode.com/problems/android-unlock-patterns/discuss/475868/Python-DFS-readable-code.
        
        def getValidWays(num,count):
            nonlocal validPatterns
            
            if m<=count<=n:
                validPatterns+=1
            
            if count==n:
                return
            
            
            self.visited.add(num)
            
            
            for nextNum in range(1,10):
                if nextNum not in self.visited:
                    
                    if (num,nextNum) in has_obstacle and has_obstacle[(num,nextNum)] not in self.visited:
                        continue         
                    
                    getValidWays(nextNum,count+1)
                    
            self.visited.remove(num)
        
        has_obstacle = {(1,3):2, (1,7):4, (1,9):5, (2,8):5, (3,7):5, (3,1):2, (3,9):6, (4,6):5, (6,4):5, (7,1):4, (7,3):5, (7,9):8, (8,2):5, (9,7):8, (9,3):6, (9,1):5}
        
        validPatterns = 0
        
        for num in range(1,10):
            self.visited = set()
            getValidWays(num,1)
            
        
            
        return validPatterns