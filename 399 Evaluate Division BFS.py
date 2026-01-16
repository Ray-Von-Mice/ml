class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #  mapping: a -> [b, value(a/b)]; b -> [a, 1/value(a/b)]; b -> [(a, 1/value)(c, value(b/c))]
        adj = defaultdict(list)
        for index, equation in enumerate(equations):
            node_a, node_b = equation[0], equation[1]
            adj[node_a].append((node_b, values[index]))
            adj[node_b].append((node_a, 1 / values[index]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            travel = deque()
            travel.append((src, 1))
            visit = set()
            visit.add(src)

            while travel:
                cur = travel.popleft()
                node, cal = cur[0], cur[1]
                if node == target:
                    return cal

                for neb, n_cal in adj[node]:
                    if neb in visit:
                        continue
                    travel.append((neb, cal * n_cal))
                    visit.add(neb)
            return -1
        
        result = []
        for query in queries:
            result.append(bfs(query[0], query[1]))

        return result