class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        out = ''
        for s in strs:
            out += str(len(s)) + '#' + s
        return out

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        out = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            
            out.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return out

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
