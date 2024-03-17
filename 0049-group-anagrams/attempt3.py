class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)

        for s in strs:
            alphabet_count = [0] * 26

            for c in s:
                alphabet_count[ord(c) - ord('a')] += 1
            strs_dict[tuple(alphabet_count)].append(s)

        return strs_dict.values()
        
