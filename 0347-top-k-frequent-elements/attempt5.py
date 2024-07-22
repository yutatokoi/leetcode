class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = collections.defaultdict(int)

        for n in nums:
            frequencies[n] += 1

        frequency_array = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(frequency_array[i][0])

        return res
        
        
