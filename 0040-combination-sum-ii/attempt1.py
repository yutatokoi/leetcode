class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()

        combination = []

        def dfs(i):
            if i >= len(candidates):
                if sum(combination) == target:
                    res.add(combination.copy())
                return

            combination.append(candidates[i])
            dfs(i + 1)

            combination.pop()
            dfs(i + 1)

        dfs(0)

        return list(res)

