class Solution:
    def climbStairs(self, n: int) -> int:
        
         # similar to finding nth fibonacci sequence
        """
        Fibonacci sequence:
        0 1 1 2 3 5 8 13 21 34
        
        # climb stairs:
        1: 1
        2: [1 + 1],[2] = 2
        3: [1+1+1],[2+1],[1+2] = 3
        4: [1+1+1+1],[2+2],[1+2+1],[2+1+1],[1+1+2] = 5
        
        so the pattern is like fibonacci series,
        if we find out the nth term of the fibonacci series, we should be 
        getting our solution
        """
        # base case:
        if n==1:
            return 1
        first_element = 1
        second_element = 2
        
        for i in range(3,n+1):
            temp = first_element + second_element
            first_element = second_element
            second_element = temp
            
        return second_element