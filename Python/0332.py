class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        res = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            res.append(airport)
        
        dfs("JFK")
        
        return res[::-1]

        
