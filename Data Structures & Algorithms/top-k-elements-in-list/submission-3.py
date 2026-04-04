class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # populate count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # populate freq
        for num, ct in count.items():
            freq[ct].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            while freq[i] and len(res) < k:
                res.append(freq[i].pop())
        
        return res


