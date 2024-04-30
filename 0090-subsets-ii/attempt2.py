class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        nums = sorted(nums)

        def dfs(i):
            if nums[i] == nums[i - 1]:
                i += 1
                
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)

        return list(res)

        
