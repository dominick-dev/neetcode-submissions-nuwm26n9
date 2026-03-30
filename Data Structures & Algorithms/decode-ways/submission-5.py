class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            # check cache
            if i in dp:
                return dp[i]
            # no ways from here
            if s[i] == '0':
                return 0
            
            # try decoding one digit
            res = dfs(i + 1)

            # try decoding two digits
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2'
                and s[i + 1] < '7')):
                    res += dfs(i + 2)

            dp[i] = res
            return res
        
        return dfs(0)
        
