class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []

        for word in words:
            if set(word.lower()) <= set("qwertyuiop"):
                res.append(word)
            elif set(word.lower()) <= set("asdfghjkl"):
                res.append(word)
            elif set(word.lower()) <= set("zxcvbnm"):
                res.append(word)

        return res
