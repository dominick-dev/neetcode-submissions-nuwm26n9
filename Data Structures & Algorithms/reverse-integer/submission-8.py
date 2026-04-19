class Solution:
    def reverse(self, x: int) -> int:
        # set min and max ranges
        MIN = -1 * (2**31)
        MAX = (2**31 - 1)

        res = 0
        while x:
            # grab rightmost digit
            digit = int(math.fmod(x, 10))
            # remove digit from x
            x = int(x / 10)

            # check that res will not be too large
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            # check that res will not be too small
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            
            # shift res left by 1, add next digit
            res = (res * 10) + digit
        
        return res

