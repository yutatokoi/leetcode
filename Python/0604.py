class StringIterator:

    def __init__(self, compressedString: str):
        self.letters = []
        self.count = []

        curr = ""
        for char in compressedString:
            if char.isdigit():
                curr += char
            else:
                self.letters.append(char)
                if curr:
                    self.count.append(int(curr))
                    curr = ""
        self.count.append(int(curr))
        self.idx = 0

    def next(self) -> str:
        res = " "
        if self.hasNext():
            res = self.letters[self.idx]
            self.count[self.idx] -= 1

            if self.count[self.idx] == 0:
                self.idx += 1

        return res

    def hasNext(self) -> bool:
        return len(self.count) > self.idx and self.count[self.idx] > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
