class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.curr_size = 0
        self.size = size
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.curr_size += 1
        while len(self.q) > self.size:
            self.q.popleft()
            self.curr_size -= 1
        return sum(self.q) / self.curr_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
