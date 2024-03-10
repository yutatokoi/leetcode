class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for chars in s:
                count[ord(chars) - ord("a")] += 1
            
            strs_dict[tuple(count)].append(s)

        return strs_dict.values()
        
