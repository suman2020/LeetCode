class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        """
        -> add characters to the stack(list)
        -> if found '#', pop the character from the stack
        -> return the string 
        -> repeat same steps 1,2,3 for the other string
        -> if equal return true else false
        
        """
        def helper(strs):
            ans= []
            
            for character in strs:
                
                if character != '#':
                    ans.append(character)
                else:
                    if not ans:
                        continue
                    ans.pop()
            return "".join(ans) # converts list to string
        
        return helper(s) == helper(t)
                    
                    
                
        