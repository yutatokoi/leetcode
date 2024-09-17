class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        common = s1.split() + s2.split()

        freq_count = collections.defaultdict(int)

        for word in common:
            freq_count[word] += 1
        
        uncommon = [word for word, count in freq_count.items() if count == 1]

        return uncommon
        
        
