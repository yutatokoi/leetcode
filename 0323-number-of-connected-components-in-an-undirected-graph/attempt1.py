class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # All nodes are individual components
        if not edges:
            return n

        components = 0
        visited = set()
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, prev):
            if i in visited:
                return 0
            
            visited.add(i)

            for neighbour in adj[i]:
                if neighbour == prev:
                    continue
                if not adj[i] or adj[i] == [prev]:
                    components += 1
                if not dfs(neighbour, i):
                    return 0

        for i in range(n):
            dfs(i, -1)

        return components


