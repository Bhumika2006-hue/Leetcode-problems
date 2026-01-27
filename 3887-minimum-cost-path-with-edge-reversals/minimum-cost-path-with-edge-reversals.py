from typing import List
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        
        # Build transformed graph
        for u, v, w in edges:
            g[u].append((v, w))      # normal
            g[v].append((u, 2 * w))  # reversed
        
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        
        pq = [(0, 0)]
        
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            
            for v, w in g[u]:
                if dist[v] > cost + w:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))
        
        return dist[n-1] if dist[n-1] < INF else -1
