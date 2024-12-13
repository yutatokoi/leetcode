class Solution:
    def toLowerCase(self, s: str) -> str:
        s_list = []
        for i in range(len(s)):
            if (ord('A') <= ord(s[i])) and (ord(s[i]) <= ord('Z')):
                s_list.append(chr(ord('a') + ord(s[i]) - ord('A')))
            else:
                s_list.append(s[i])

        return "".join(s_list)
