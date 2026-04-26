class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(sring):
            l, r = 0, len(sring) - 1
            while l < r:
                if sring[l] != sring[r]:
                    return False
                l += 1
                r -= 1 
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return check(s[l+1:r+1]) or check(s[l:r])

            l += 1
            r -= 1        
        
        return True
            

        