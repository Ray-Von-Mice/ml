class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        n = len(candidates)
        def dfs(indx, total):

            if total == target:
                res.append(subset[:])
                return
            
            if indx == n or total > target:
                return
            
            # include current index number and explore with it
            subset.append(candidates[indx])
            dfs(indx, total + candidates[indx])
            # exclude current index number and explore without it
            subset.pop()
            dfs(indx + 1, total)

        dfs(0, 0)
        return res