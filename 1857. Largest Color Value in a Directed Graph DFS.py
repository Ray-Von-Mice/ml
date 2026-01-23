class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]
        result = 0
        for src, dst in edges:
            adj[src].append(dst)
        
        visit, cur_path = set(), set()
        colors_freqList = [[0] * 26 for _ in range(n)]
        # 3: blue 1, red 1, purple 0
        # 2: blue 0 + max(neighbor blue), red 1 + max(neighbor red), purle 0 + max(neigbor purple)
        def dfs(cur):
            if cur in cur_path:
                return -1
            if cur in visit:
                return 0

            visit.add(cur)
            cur_path.add(cur)
            color_index = ord(colors[cur]) - ord('a')
            colors_freqList[cur][color_index] = 1
            for neb in adj[cur]:
                neb_cFreq = dfs(neb)
                if neb_cFreq == -1:
                    return -1
                for colr in range(26):
                    cur_freq = 1 if colr == color_index else 0
                    colors_freqList[cur][colr] = max(cur_freq + colors_freqList[neb][colr],
                    colors_freqList[cur][colr])
            
            cur_path.remove(cur)
            max_color_freq = max(colors_freqList[cur])
            return max_color_freq

        result = 0
        for node in range(n):
            node_result = dfs(node)
            if node_result == -1:
                return -1
            result = max(result, node_result)
        
        return result