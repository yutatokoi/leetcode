class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse=True)
        rankings = dict()

        for i in range(len(sortedScore)):
            if i == 0:
                rankings[sortedScore[i]] = "Gold Medal"
            elif i == 1:
                rankings[sortedScore[i]] = "Silver Medal"
            elif i == 2:
                rankings[sortedScore[i]] = "Bronze Medal"
            else:
                rankings[sortedScore[i]] = str(i + 1)

        answer = []

        for s in score:
            answer.append(rankings[s])

        return answer
