class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        index_sum = dict()

        for i, r in enumerate(list1):
            if r in common:
                index_sum[r] = i

        for i, r in enumerate(list2):
            if r in common:
                index_sum[r] += i

        min_sum = min(index_sum.values())

        return [r for r, s in index_sum.items() if s == min_sum]
