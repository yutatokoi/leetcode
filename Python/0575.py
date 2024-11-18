class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        uniqueCandies = set(candyType)
        if len(uniqueCandies) < len(candyType) // 2:
            return len(uniqueCandies)
        
        return len(candyType) // 2
