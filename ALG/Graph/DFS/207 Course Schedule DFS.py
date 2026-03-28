class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, preq in prerequisites:
            adj[crs].append(preq)
        
        result = []
        visit = set()
        cycle = defaultdict(int)
        def dfs(node):
            if cycle[node] > 0:
                return False
            if node in visit:
                return True
            
            cycle[node] += 1
            for ne in adj[node]:
                if dfs(ne) == False:
                    return
            cycle[node] -= 1
            visit.add(node)
            result.append(node)
            return True
        
        for i in range(numCourses):
            # cycle detected
            if dfs(i) == False:
                return []
        
        return result