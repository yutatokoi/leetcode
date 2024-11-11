class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for total in dp:
                next_dp.add(total + nums[i])
                next_dp.add(total)

            dp = next_dp

        return target in dp




        
