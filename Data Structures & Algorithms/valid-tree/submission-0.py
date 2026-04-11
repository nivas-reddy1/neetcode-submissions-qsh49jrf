class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Base case: an empty graph technically counts as a tree
        if n == 0:
            return True
            
        # Create an adjacency list mapping each node to an empty list
        adj = {i: [] for i in range(n)}
        
        # Populate the adjacency list (undirected means edges go both ways)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        
        # DFS function to detect cycles
        def dfs(i, prev):
            # If node is already visited, a cycle is detected
            if i in visit:
                return False
                
            visit.add(i)
            
            # Check all neighbors of the current node
            for j in adj[i]:
                # Skip the node we just came from to prevent false cycle detection
                if j == prev:
                    continue
                # If a cycle is detected down the path, return False
                if not dfs(j, i):
                    return False
                    
            return True
            
        # 1. Check if dfs(0, -1) returns True (no cycles)
        # 2. Check if len(visit) == n (the graph is fully connected)
        return dfs(0, -1) and n == len(visit)