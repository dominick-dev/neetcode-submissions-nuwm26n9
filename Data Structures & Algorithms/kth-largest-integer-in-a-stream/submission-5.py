class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = nums
        self.k = k
        heapq.heapify(self.hp)
        # min heap, len hp = k means kth is at top of heap
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)


    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        # pop until len(hp) == k
        # DONT pop if len(hp) < k
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]


        
