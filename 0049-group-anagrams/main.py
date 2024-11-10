class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = collections.defaultdict(list)
        for s in strs:
            letters["".join(sorted(list(s)))].append(s)

        return letters.values()

        
