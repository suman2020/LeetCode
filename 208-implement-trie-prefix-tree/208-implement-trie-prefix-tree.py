class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    # https://www.youtube.com/watch?v=oobqoCJlHA0
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
                
            current = current.children[c]
            
        current.endOfWord = True

    def search(self, word: str) -> bool:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)