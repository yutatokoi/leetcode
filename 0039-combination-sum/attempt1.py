class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        def dfs(i, combination, combination_sum):
            if combination_sum == target:
                res.append(combination.copy())
                return
            
            if i >= len(candidates) or combination_sum > target:
                return

            combination.append(candidates[i])
            dfs(i, combination, combination_sum + candidates[i])
            combination.pop()
            dfs(i + 1, combination, combination_sum)

        dfs(0, [], 0)
        return res

