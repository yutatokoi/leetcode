class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            for j in range(len(prefix)):
                if ((j < len(word)) and (prefix[j] == word[j])):
                    continue
                else:
                    prefix = prefix[:j]
                    break

        return prefix

        
