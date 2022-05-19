class Solution:
    def fib(self, n: int) -> int:
        # Recursive solution
        """
        cache_dict = {} #to avoid repeated calculations
        
        def recurse_fib(N):
            
            if N in cache_dict:
                return cache_dict[N]
            
            if N < 2:
                result = N
                
            else:
                result = recurse_fib(N-1) + recurse_fib(N-2)
                
            cache_dict[N] = result
            
            return result
            
        
        
        return recurse_fib(n)
        """
        # iterative solution:
        if (n <= 1):
            return n

        current = 0
        prev1 = 1
        prev2 = 0

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
        
        
        
        