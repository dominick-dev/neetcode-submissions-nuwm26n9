class Solution:
    def reverse(self, x: int) -> int:
        # copy x for reference later
        org = x
        # ignore case
        x = abs(x)
        # set result to reverse x
        res = int(str(x)[::-1])

        # invert res if org is neg
        if org < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        
        return res
