class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        if len(edges) != n - 1:
            return False
        
        visited = set()

        for node in range(n):
            if node in visited:
                continue
            
            queue = deque([(node, -1)])
            visited.add(node)
            while queue:
                node, parent = queue.popleft()
                visited.add(node)
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, node))
                    elif nei != parent:
                        return False
        
        return True