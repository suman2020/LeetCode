class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
    
        
        """             k=1
                         0                         N=1
                  k=1       k=2            
                   0         1                     N =2 
                   
               k=1  k=2    k=3   k=4    
                     
                0    1      1        0                N=3
                  
           k=1  (2)(3)(4) (5)(6)   (7) (8)  
             0   1  1  0  1   0    0   1             N=4
             
             
           For the Kth symbol on the nth row: kthGrammer(N,K)
           we can see a pattern from its parent row (n-1)th row. 
           eg: for k=7 or k=8 in n=4 row, kth of parent(n=3) is 4. so there is a upper division
           parent = kthGrammer(N-1,k+1//2) 
           
           
            Intutition:
            
            if parent ==0:
                if      k of current row is odd:  return 0
                else    k of current row is even: return 1
                
            if parent ==1:
                if      k of current row is odd:  return 1
                else    k of current row is even: return 0
    
            
            
            
        
        
        """
        
        if n==1:
            return 0
        
        parent = self.kthGrammar(n-1,k//2 +  k%2) # 3//2 + 3%2 = 1 + 1 = 2 ;    4//2 + 4%2 = 2+ 0 = 2
        
        is_K_Odd = (k %2 ==1)
        
        if parent is 1:
            return 1 if is_K_Odd else 0
        
        else:
            return 0 if is_K_Odd else 1
        
       
        
        