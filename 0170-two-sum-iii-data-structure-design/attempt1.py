class TwoSum:

    def __init__(self):
        self.array = []
        

    def add(self, number: int) -> None:
        self.array.append(number)
        

    def find(self, value: int) -> bool:
        nums = sorted(self.array)
        l = 0
        r = len(nums) - 1
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == value:
                return True
            elif two_sum < value:
                l += 1
            elif two_sum > value:
                r -= 1

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
