class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = { i : [] for i in range(N) }
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([manhattan_dist, j])
                adj[j].append([manhattan_dist, i])

        res = 0
        visited = set()
        minHeap = [[0, 0]] # [cost, node]

        while len(visited) < N:
            cost, node = heapq.heappop(minHeap)
            
            if node in visited:
                continue
            
            res += cost
            visited.add(node)
            for neighbor_cost, neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [neighbor_cost, neighbor])

        return res

        
