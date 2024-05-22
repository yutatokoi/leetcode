class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for neighbour in adj[i]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, i):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visited)

        
