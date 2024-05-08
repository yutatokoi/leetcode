class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            distances.append([p[0] ** 2 + p[1] ** 2, p[0], p[1]])

        heapq.heapify(distances)

        res = []
        i = 0
        while i < k:
            closest = heapq.heappop(distances)
            res.append([closest[1], closest[2]])
            i += 1

        return res

        
    
