class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 or n == 1:
            return False
        
        average = total // 2
        # memo for memo[i][target] -> can target be reached from nums[i] (with or without)
        memo = [[-1] * (average + 1) for _ in range(n + 1)]

        def dfs(indx, remain):
            if remain == 0:
                return True
            if indx >= n or remain < 0:
                return False
            
            if memo[indx][remain] != -1:
                return memo[indx][remain]
            
            # remain (average) can be calculated without or with current num at indx
            memo[indx][remain] = dfs(indx + 1, remain) or dfs(indx + 1, remain - nums[indx])

            return memo[indx][remain]
        
        return dfs(0, average)