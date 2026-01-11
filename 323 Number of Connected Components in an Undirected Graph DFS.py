class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visit = set()
        numComp = 0

        def dfs(cur):
            if cur in visit:
                return
            visit.add(cur)
            for neb in graph[cur]:
                dfs(neb)

        for i in range(n):
            if i not in visit:
                numComp += 1
                dfs(i)
        return numComp