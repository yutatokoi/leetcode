from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_indices = defaultdict(list)

        for i in range(len(nums2)):
            nums2_indices[nums2[i]].append((False, i))

        mapping = []

        for n in nums1:
            indices = nums2_indices[n]
            i = 0
            seen, index = indices[i]
            while seen:
                i += 1
                seen, index = indices[i]

            indices[i] = (True, index)

            mapping.append(index)

        return mapping
