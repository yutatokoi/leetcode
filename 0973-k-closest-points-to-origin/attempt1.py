class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            distances.append([distance, [points[i][0], points[i][1]]])

        min_heap = heapq.heapify(distances)
        
        res = []
        i = 0
        while i < k:
            closest = heapq.heappop(min_heap)
            res.append(closest[1])
            i += 1

        return res

        
