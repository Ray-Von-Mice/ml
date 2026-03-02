class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        chosen = [False] * n
        result, perm = [], []

        def dfs():
            if len(perm) == n:
                result.append(perm[:])
                return
            
            for i in range(n):
                if not chosen[i]:
                    perm.append(nums[i])
                    chosen[i] = True
                    dfs()
                    perm.pop()
                    chosen[i] = False
        
        dfs()
        return result