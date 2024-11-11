class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].islower():
            for ch in word:
                if ch.isupper():
                    return False
        elif word[1].islower():
            i = 2
            while i < len(word):
                if word[i].isupper():
                    return False
                i += 1
        elif word[1].isupper():
            for ch in word:
                if ch.islower():
                    return False

        return True
