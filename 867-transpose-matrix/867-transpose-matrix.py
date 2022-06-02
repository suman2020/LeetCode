class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        transpose = []
        for col in range(COLS):
            new_row = []
            
            for row in range(ROWS):
                new_row.append(matrix[row][col])
                
            transpose.append(new_row)
                
        return transpose
    
        """
        0,0   0,1   0,2
        1,0   1,1   1,2
        2,0   2,1   2,2
        
        # we have to convert it to
        0,0   1,0   2,0
        
        so its better to have row in inner loop
        
        """
                
                
                
        