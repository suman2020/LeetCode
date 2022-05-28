class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # details in notes
        res = []
        
        def backtrack(start,comb):
            
            # print("comb" ,comb)
            # print("res",res)
            if len(comb) ==k:
                res.append(comb.copy())  # since list is an object, we modify it in other recursive calls, so we have a copy of it, if copy is not used then our result is messed up with the latest object
                
                return
            
            for i in range(start,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
                
        backtrack(1,[])
        
        return res
    
        # time complexity: k.n^k