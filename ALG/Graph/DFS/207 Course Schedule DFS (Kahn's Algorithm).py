class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        reqNum = [0] * numCourses
        for crs, preq in prerequisites:
            reqNum[preq] += 1
            adj[crs].append(preq)
        
        result = []
        visit = set()
        cycle = defaultdict(int)
        def dfs(node):
            if cycle[node] > 0:
                return
            if node in visit:
                return
            
            visit.add(node)
            cycle[node] += 1
            result.append(node)
            for ne in adj[node]:
                reqNum[ne] -= 1
                if reqNum[ne] == 0:
                    dfs(ne)
            cycle[node] -= 1
            return
        
        for i in range(numCourses):
            if reqNum[i] == 0:
                dfs(i)
        
        if len(result) != numCourses:
            return []
        return result[::-1]