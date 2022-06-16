class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # https://www.youtube.com/watch?v=JtpGVqbiegQ
        n = len(seats)
        empty = 0
        result = 0
        idx1, idx2 = -1,-1
        
        for i in range(n):
            if seats[i]==1:
                empty = 0
                
                if idx1 == -1:
                    idx1 = i 
                    
                idx2 = i
                
            else:
                empty+=1
                result = max(result,(empty+1)//2)
                
        result = max(result,idx1,n-1-idx2)
        
        return result
    
        """
        Two cases:
        Alex can be inserted: at edges or internally(between edges)
        
        Internal cases:
        1 0 0 0 0 0 0 1 --> ans = 6+1/2 = 3
        1 0 0 0 0 0 1   --> ans = 5+1//2 = 3
        1 0 0 0 0 1     --> ans = 4+1//2 = 2   
        1 0 0 0 1       --> ans = 3+1//2 = 2
        1 0 0 1         --> ans = 2+1//2 = 1
        1 0 1           --> ans = 1+1 //2 = 1
        
        Intuition: count the number of internal zeros: 
        
        
        Edge cases:
        
        i   0 1 2 3
            0 0 0 1 --> ans = 3 (first occurance of i)
        
        i   0 1 2 3 4 5 6 7 8 9
            1 0 1 1 0 0 0 0 0 0 --> ans =  10 - 3 - 1 = 6 (n - lastoccuranceofone-1)
            
        
        Final ans = max(first_occurance_of_1 , size - last_occurance_of_1 - 1, no_of_consecutive_zeros + 1 // 2)
        
        Sample example: 
        
        i   0 1 2 3 4 5 6 7 8 9 10 11 12 13  14
            0 0 0 0 1 0 0 0 0 1  0  0  0  0  0 
            
            size = 15
            first_occurance_of_1 = 4
            last_occurance_of_1 = 9 --> size - 9 - 1 = 15-9-1 = 5
            no_of_max_consecutive_zeros = 4 // 2 = 2
            ans = max(4,5,2) --> 5
            
        
        """
    
                
            
        
        
        