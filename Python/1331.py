class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_elements = sorted(list(set(arr)))

        ranks = dict()
        rank = 1
        for n in sorted_elements:
            ranks[n] = rank
            rank += 1

        ans = []
        for n in arr:
            ans.append(ranks[n])

        return ans

        
