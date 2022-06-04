class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
#         size = len(wordsDict)
#         index1, index2 = size, size
#         ans = size

#         for i in range(size):
#             if wordsDict[i] == word1:
#                 index1 = i
#                 ans = min(ans, abs(index1-index2))
#             elif wordsDict[i] == word2:
#                 index2 = i
#                 ans = min(ans, abs(index1-index2))
#         return ans

        index1 = -1
        index2 = -1
        size = len(wordsDict)
        ans = size
        for i in range(size):
            if wordsDict[i] == word1:
                index1 = i
                
            elif wordsDict[i] == word2:
                index2 = i
                
            if index1 !=-1 and index2 !=-1:
                ans = min(ans,abs(index2-index1))
                
        return ans

        
    
            
        