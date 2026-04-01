class Solution:
    def dfs(self, node, adj, visited):
        if node in visited:
            return
        
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                self.dfs(nei, adj, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        components = 0
        for i in range(n):
            if i not in visited:
                self.dfs(i, adj, visited)
                components += 1
        
        return components