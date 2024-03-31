class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = dict()
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        l = 0
        while l < len(s) - len(t):
            r = len(t)
            while r < len(s) - len(t):
                s_substring = s[l : r]
                s_substring_count = dict()
                for char in s_substring:
                    if char in s_substring_count:
                        s_substring_count[char] += 1
                    else:
                        s_substring_count[char] = 1
                
                matches = 0
                for key in t_count.keys():
                    if key in s_substring_count and t_count[key] == s_substring_count[key]:
                        matches += 1
                    else:
                        matches += 0
                if matches == len(t):
                    return True
                else:
                    continue

                r += 1
                
            l += 1
        
        return ""

