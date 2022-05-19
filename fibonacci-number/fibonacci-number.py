class Solution:
    def fib(self, n: int) -> int:
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
        