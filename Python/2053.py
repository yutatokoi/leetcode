class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_map = dict()
        
        for s in arr:
            if s in distinct_map:
                distinct_map[s] = False
            else:
                distinct_map[s] = True

        for s in arr:
            if distinct_map[s]:
                k -= 1
                if k == 0:
                    return s

        return ""

