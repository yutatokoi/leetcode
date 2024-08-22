class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        mask = "".join(["1"] * len(binary))
        
        binary = int(binary, 2)
        mask = int(mask, 2)

        return binary ^ mask
        
        
