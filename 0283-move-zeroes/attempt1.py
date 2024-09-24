class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1

        for _ in range(zero_count):
            nums.remove(0)
            nums.append(0)

        return

        
