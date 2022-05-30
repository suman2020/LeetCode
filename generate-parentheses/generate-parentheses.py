class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # only add open parantheese if open < n
        # only add a closing parantheses if closed < open
        # valid iff ope == closed ==n
        
        # https://www.youtube.com/watch?v=s9fokUqJ76A
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            
            if openN ==closedN ==n:
                res.append("".join(stack))
                
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
                
        backtrack(0,0)
        
        return res
            
                
            
                
                
            
        
        
         