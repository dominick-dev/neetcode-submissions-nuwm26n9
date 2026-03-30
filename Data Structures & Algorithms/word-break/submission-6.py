class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s), -1, -1):
            if dp[i] == True:
                for word in wordDict:
                    word_len = len(word)
                    if (i - word_len >= 0 
                        and s[i - word_len:i] == word):
                        dp[i - word_len] = True
        
        return dp[0]
                