class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix_sums = {0: 1} # key:sum val: frequency

        # iterate through nums
        for n in nums:
            # update curr sum
            curr_sum += n
            # get sum needed to satisfy k
            need = curr_sum - k

            # add need freq to res
            res += prefix_sums.get(need, 0)
            # update mp with current sum
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        
        return res
