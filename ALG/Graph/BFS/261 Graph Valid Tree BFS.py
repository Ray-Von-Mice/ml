class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visit = set()
        visit.add(0)
        travel = deque()
        travel.append((0, -1))

        while travel:
            cur, pre = travel.popleft()
            
            for neb in graph[cur]:
                if neb == pre:
                    continue
                if neb in visit:
                    return False
                visit.add(neb)
                travel.append((neb, cur))

        return len(visit) == n