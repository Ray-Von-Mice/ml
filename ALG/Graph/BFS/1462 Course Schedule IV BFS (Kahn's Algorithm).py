class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not queries:
            return []
        adj = defaultdict(list)
        reqNum = [0] * numCourses
        for preq, crs in prerequisites:
            adj[crs].append(preq)
            reqNum[preq] += 1
        
        traverse = deque()
        for i in range(numCourses):
            if reqNum[i] == 0:
                traverse.append(i)
        
        reqMe = [set() for _ in range(numCourses)]

        while traverse:
            cur = traverse.popleft()

            for preq in adj[cur]:
                # update cur to its preq, also add those who required cur
                reqMe[preq].add(cur)
                reqMe[preq] |= reqMe[cur]
                reqNum[preq] -= 1
                if reqNum[preq] == 0:
                    traverse.append(preq)
        result = []
        for preq, crs in queries:
            if crs in reqMe[preq]:
                result.append(True)
            else:
                result.append(False)
        return result