class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        memo = [0] * n

        def dfs(indx):
            if memo[indx] != 0:
                return memo[indx]
            
            increm = 1
            for i in range(indx + 1, n):
                if nums[indx] < nums[i]:
                    increm = max(increm, 1 + dfs(i))
            
            memo[indx] = increm
            return increm
        
        result = [dfs(j) for j in range(n)]
        return max(result)