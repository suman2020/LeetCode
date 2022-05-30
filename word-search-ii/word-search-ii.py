# https://www.youtube.com/watch?v=asbcE9mZz_U
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()  
            curr = curr.children[c]
               
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        
        res, visit = set(), set()
        
        def dfs(r,c,node, word):
            
            if r<0 or c<0 or r ==ROWS or c==COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            
            node = node.children[board[r][c]]
            word +=board[r][c]
            
            if node.isWord:
                res.add(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
                
        return list(res)
        
        
        
        
        
        
        """
        rows = len(board)
        cols = len(board[0])
        return_list = set()
        for row in range(rows):
            for col in range(cols):
                
                for word in words:
                    
                    if board[row][col] == word[0]and self.search(board, row, col, 0, word):
                        return_list.add(word)
                
                
        return list(return_list)
    
    
    def search(self, board, r, c, index, word):
        
        if index == len(word):
            return True
        
        if r < 0 or r>=len(board) or c < 0 or c>=len(board[0]) or board[r][c] !=word[index]:
            return False
        
        temp= board[r][c]
        board[r][c] = " "
        
        found = self.search(board, r+1,c,index+1, word) or self.search(board,r-1,c, index+1, word) or self.search(board, r,c+1,index+1, word) or self.search(board,r,c-1, index+1, word)
        
        board[r][c] = temp
        
        return found 
        
        """
        
        
        
        
        
        