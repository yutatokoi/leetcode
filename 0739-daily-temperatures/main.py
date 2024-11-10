class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [(0, temperatures[0])]

        for i in range(1, len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                index, temp = stack.pop()
                answer[index] = i - index

            stack.append((i, temperatures[i]))

        return answer

        
