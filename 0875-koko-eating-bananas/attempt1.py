class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_bananas = sum(piles)
        min_k = total_bananas // len(piles)
        max_k = max(piles)
        possible_k = list(range(min_k, max_k + 1))

        l = 0
        r = len(possible_k) - 1

        while l <= r:
            m = (l + r) // 2
            if self.will_finish(possible_k[m], piles) == h:
                return possible_k[m]
            elif self.will_finish(possible_k[m], piles) > h:
                l = m + 1
            elif self.will_finish(possible_k[m], piles) < h:
                return possible_k[m]

    def will_finish(self, k, piles):
        hours = 0
        for i in range(len(piles)):
            hours += (piles[i] / k)
        return int(hours + 1)

