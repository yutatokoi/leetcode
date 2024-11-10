class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for n in details:
            if int(n[11:13]) > 60:
                res += 1

        return res

        
