class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        dist = [float('inf')] * (n + 1)
        # dummy 
        dist[0] = float('-inf')

        for par, n, w in times:
            adj[par].append((n, w))
        
        def dfs(cur, time):
            if time >= dist[cur]:
                return
            
            dist[cur] = time
            for neb, travelTime in adj[cur]:
                dfs(neb, travelTime + time)
            
        dfs(k, 0)
        min_time = max(dist)
        return min_time if min_time < float('inf') else -1