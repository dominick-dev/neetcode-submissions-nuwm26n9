class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first, second = heapq.heappop_max(stones), heapq.heappop_max(stones)
            result = abs(first - second)
            heapq.heappush_max(stones, result)
        
        return stones[0]

        