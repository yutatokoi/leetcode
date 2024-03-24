class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            j = 0
            while i + j < len(temperatures) and temperatures[i + j] <= temperatures[i]:
                j += 1
            if i + j == len(temperatures) - 1:
                result.append(0)
            else:
                result.append(j)
                
        return result

