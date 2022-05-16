class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        return_rw = [1]
        
        for i in range(rowIndex):
            for j in range( i,0,-1):
                
                return_rw[j] = return_rw[j-1] + return_rw[j]
                
            return_rw.append(1)
            
            print(return_rw)
            
        return return_rw
    
        
        """
        if row_index = 1
        
        return_rw = [1]
        
        for i in range(1):
            for j in range(i,0,-1):
            
            return_rw.append(1)
            
        return_rw = [1,1]
            
        1st iteration: i = 0
        so second for loop does not get iterated
        
        if row_index = 2
        
        for i in range()
            

        
        """
            