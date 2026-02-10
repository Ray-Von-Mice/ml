class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_l = defaultdict(list)
        for node_a, node_b in edges:
            adj_l[node_a].append(node_b)
            adj_l[node_b].append(node_a)

        edges_nums = defaultdict(int)
        leaves = deque()
        for node, edges in adj_l.items():
            edges_nums[node] = len(edges)
            if len(edges) == 1:
                leaves.append(node)

        result = []
        while leaves:
            if n <= 2:
                while leaves:
                    result.append(leaves.popleft())
                return result
            else:
                for _ in range(len(leaves)):
                    cur = leaves.popleft()
                    n -= 1
                    for neb in adj_l[cur]:
                        edges_nums[neb] -= 1
                        if edges_nums[neb] == 1:
                            leaves.append(neb)