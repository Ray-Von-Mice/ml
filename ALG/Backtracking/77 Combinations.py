class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, subset = [], []

        def depthFS(cur):
            if len(subset) == k:
                result.append(subset[:])
                return
            
            for i in range(cur, n):
                subset.append(i + 1)
                depthFS(i + 1)
                subset.pop()

        depthFS(0)
        return result