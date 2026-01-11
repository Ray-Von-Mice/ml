class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visit = set()

        # return false if a cycle is found, true if there is no cycle
        def dfs(cur, pre) -> bool:
            if cur in visit:
                return False
            
            visit.add(cur)
            for neb in graph[cur]:
                if neb == pre:
                    continue
                if not dfs(neb, cur):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n