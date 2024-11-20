from collections import defaultdict as dd

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lhs = 0
        hashmap = dd(int)

        for n in nums:
            hashmap[n] += 1

        for key in hashmap:
            if key + 1 in hashmap:
                lhs = max(lhs, hashmap[key] + hashmap[key + 1])

        return lhs
