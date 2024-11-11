class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0

        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i+1] - timeSeries[i])
        
        total += duration

        return total
