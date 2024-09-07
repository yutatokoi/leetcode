class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = dict()
        vals = set()
        
        for i in range(len(s)):
            if s[i] in chars:
                if chars[s[i]] != t[i]:
                    return False
            else:
                if t[i] in vals:
                    return False
                chars[s[i]] = t[i]
                vals.add(t[i])

        return True


