# attempt1 (naive solution)
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            elif [sentence1[i], sentence2[i]] in similarPairs or [sentence2[i], sentence1[i]] in similarPairs:
                continue
            else:
                return False

        return True

# attempt2 (hashmap solution)
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        word_to_similar_words = collections.defaultdict(set)

        for word1, word2 in similarPairs:
            word_to_similar_words[word1].add(word2)
            word_to_similar_words[word2].add(word1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in word_to_similar_words[sentence1[i]]:
                continue
            return False

        return True
