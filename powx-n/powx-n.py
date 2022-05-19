class Solution:
    def myPow(self, x: float, n: int) -> float:
        # iterative solution:
        """
        x = 3, n = 5
        result = 1
        while 5:
            5%2 == 1: result = result * x = 1 * 3 = 3
            x = x * x = 3 *3 = 9
            n = n//2 = 5 //2 = 2
        while 2:
            2%2==0: not executed
            x = x*x = 9*9 = 81
            n = n//2 = 2//2 = 1
            
        while 1:
            1 % 2 ==1:
                result = result * x = 3 * 81 = 243
                
            x = x *x = 81 * 81 = ..
            1//2 = 0
            
            
        
        """
        # negative power:
        if n < 0:
            x = 1/x
            n = abs(n)
            
        result = 1
        while n:
            if n%2:
                result = result * x
                
            x = x*x
            n = n//2   
        
        return result
    
    
 
        
            