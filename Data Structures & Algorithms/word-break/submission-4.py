class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bake in base case
        dp = {len(s) : True}

        def dfs(i):
            # cache hit
            if i in dp:
                return dp[i]
            
            # iter through each word
            for word in wordDict:
                # get len
                word_len = len(word)
                # check if curr word works
                if s[i:i + word_len] == word:
                    # only return true if this word is good base case
                    if dfs(i + word_len):
                        dp[i] = True
                        return True

            dp[i] = False
            return False
        
        return dfs(0)

