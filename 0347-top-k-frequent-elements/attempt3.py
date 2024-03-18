class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict()

        for n in nums:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1

        sorted_nums_dict = sorted(nums_dict.items(), key=lambda x:x[1], reverse=True)
        output = []
        i = 0
        while i < k:
            output.append(sorted_nums_dict[i][0])
            i += 1

        return output

