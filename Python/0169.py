class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        majority = 0

        for n in nums:
            if majority == 0:
                ans = n
            
            if n == ans:
                majority += 1
            else:
                majority -= 1
                
        return ans
        
        
