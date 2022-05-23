class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
        
        # more examples in notes
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for w in wordDict:
                if dp[i - len(w)+1] and s[i-len(w)+1:i+1] == w:
                    dp[i+1] = True
                    
        return dp[-1]
    
        """
        S--> satisfies if condition
        T --> True
        
        cats    dog     sand    cat
        
        
        0   1   2   3   4   5   6   7   8   9
        c   a   t   s   a   n   d   o   g
        |       |   |   |       |   |   |
        |       |   |   |       |   |   |
        T       S   T   T       S   T   although s[i-len(w)+1:i+1]->s[8-3+1:9]->s[6:9]-> dog==dog, the other condition is not satisfied
                    S                     dp[i-len(w)+1] = dp[8-3+1]=dp[6] = False. False at dp[6] indicates that there is not a  
                                          successful break at index 6-1 = 5(i.e at character "n")

        """
    