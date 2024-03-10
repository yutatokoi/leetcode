class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict() # Key: int | Value: count

        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        
        sorted_dict = sorted(nums_dict.items(), key=lambda x:x[1], reverse=True)

        n = 0
        answer = list()
        while n < k:
            answer.append(sorted_dict[n][0])
            n += 1
        
        return answer
        
