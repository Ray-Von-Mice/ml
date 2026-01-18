class UnionFind():
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x != self.parent[x]:
            tmp_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.rank[x] *= self.rank[tmp_parent]
        return self.parent[x]

    def union(self, x, y, value):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1.0
        if y not in self.parent:
            self.parent[y] = y
            self.rank[y] = 1.0
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.rank[root_x] = value * self.rank[y] / self.rank[x]

    def caluclate(self, x, y):
        if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
            return -1.0
        return self.rank[x] / self.rank[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = UnionFind()

        for eq, value in zip(equations, values):
            node_a, node_b = eq[0], eq[1]
            graph.union(node_a, node_b, value)
        
        result = []
        for query in queries:
            result.append(graph.caluclate(query[0], query[1]))
        
        return result