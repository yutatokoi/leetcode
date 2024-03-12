class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        hash_sorted = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)

        result = []
        n = 0

        while n < k:
            result.append(hash_sorted[n][0])
            n += 1

        return result

