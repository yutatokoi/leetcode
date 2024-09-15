class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest_distance = len(wordsDict)
        pos1, pos2 = -1, -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
            elif wordsDict[i] == word2:
                pos2 = i

            if pos1 != -1 and pos2 != -1:
                shortest_distance = min(shortest_distance, abs(pos2 - pos1))

        return shortest_distance


