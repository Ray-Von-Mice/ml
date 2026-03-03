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
                    # compare backwards to skip to first non duplicate num
                    if i and nums[i] == nums[i - 1] and not chosen[i - 1]:
                        continue
                    perm.append(nums[i])
                    chosen[i] = True
                    dfs()
                    perm.pop()
                    chosen[i] = False
        
        dfs()
        return result