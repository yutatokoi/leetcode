class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num: int) -> bool:
            num_str = str(num)
            for i in range(len(num_str)):
                if num_str[i] == '0':
                    return False
                elif num % int(num_str[i]) != 0:
                    return False

            return True

        ans = []
        for n in range(left, right + 1):
            if isSelfDividing(n):
                ans.append(n)

        return ans    
