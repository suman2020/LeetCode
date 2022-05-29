class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        # https://www.youtube.com/watch?v=xJl_PE0Wu14
        def getPrefixes(prefix):
            nonlocal prefixes
            if prefix in prefixes:
                return prefixes[prefix]
            prefixes[prefix]=[]
            
            for word in words:
                if word.startswith(prefix):
                    prefixes[prefix].append(word)
                
            return prefixes[prefix]
            
        def backtrack(index,current):
            nonlocal result
            if index == N:
                result.append(current[:])
                return 
            
            
            # debug = [word[index] for word in current]
            # print(debug)
            
            prefix = ''.join([word[index] for word in current])
            
            for candidate in getPrefixes(prefix):
                current.append(candidate)
                backtrack(index+1,current)
                current.pop()
                
        
        result = []
        N = len(words[0])
        prefixes = {}
    
        for word in words:
            backtrack(1,[word])
            
        return result
    
        # time complexity: 0(N.26^L)
                
            
        
            
        