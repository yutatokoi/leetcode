class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        if len(self.nums) < self.size:
            self.nums.append(val)
            return sum(self.nums) / len(self.nums)
        else:
            self.nums = self.nums[1:] + [val]
            return sum(self.nums) / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
