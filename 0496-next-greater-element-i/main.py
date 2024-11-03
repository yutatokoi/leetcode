class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        length = len(nums2)

        for num1 in nums1:
            i = 0
            while i < length and nums2[i] != num1:
                i += 1
            
            found = False
            while i < length:
                if nums2[i] > num1:
                    found = True
                    break
                i += 1
            
            if found:
                ans.append(nums2[i])
            else:
                ans.append(-1)

        return ans
