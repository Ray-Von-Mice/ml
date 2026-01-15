class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        REQED, NREQ, UNVIS = 1, 0, -1
        requList = [[UNVIS] * numCourses for _ in range(numCourses)]

        for preq, crs in prerequisites:
            adj[crs].append(preq)
            requList[crs][preq] = True

        def dfs(cur, curPreq):
            # if this is visited, either prequired or not
            if requList[cur][curPreq] != UNVIS:
                return requList[cur][curPreq] == REQED
            
            for neb in adj[cur]:
                if neb == curPreq or dfs(neb, curPreq):
                    requList[cur][curPreq] = REQED
                    return True # REQED
            
            requList[cur][curPreq] = NREQ
            return False # NREQ

        
        result=[]
        for u, v in queries:
            result.append(dfs(v, u))
        
        return result