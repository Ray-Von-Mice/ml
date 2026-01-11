class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rootSet = [-1] * 2001

        def unionFind(root: List[int], target):
            while root[target] != -1:
                target = root[target]
            return target

        for s, d in edges:
            a = unionFind(rootSet, s)
            b = unionFind(rootSet, d)
            if a == b:
                return [s, d]
            rootSet[a] = b
        
        return []