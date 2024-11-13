class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()

        for i in range(len(sList)):
            sList[i] = sList[i][::-1]

        return " ".join(sList)
