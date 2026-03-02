class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, subset = [], []
        n = len(candidates)
        candidates.sort()

        def depthFS(indx, cur_total):
            if cur_total == target:
                result.append(subset[:])
                return
            
            if cur_total > target or indx == n:
                return

            subset.append(candidates[indx])
            # prevent reusing current number by passing index + 1 into futher dfs
            depthFS(indx + 1, cur_total + candidates[indx])

            subset.pop()
            # skip duplicate from sorted input [1, 1, 1, 2, 6] -> index points at last 1, pos(2)
            while indx + 1 < n and candidates[indx] == candidates[indx + 1]:
                indx += 1
            # explore futher without 1, from position indx + 1
            depthFS(indx + 1, cur_total)
        
        depthFS(0, 0)
        return result