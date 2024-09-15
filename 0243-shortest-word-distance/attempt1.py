class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        positions = collections.defaultdict(list)

        for i in range(len(wordsDict)):
            positions[wordsDict[i]].append(i)

        word1_positions = positions[word1]
        word2_positions = positions[word2]
        shortest_distance = float("infinity")

        for pos1 in word1_positions:
            for pos2 in word2_positions:
                distance = abs(pos2 - pos1)

                shortest_distance = min(shortest_distance, distance)

        return shortest_distance

        
