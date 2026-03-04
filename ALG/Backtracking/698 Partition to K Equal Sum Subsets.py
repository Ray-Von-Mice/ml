class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        subsum = total // k
        nums.sort(reverse = True)
        subset = [0] * k # sum of k subsets
        def dfs(indx):
            if indx == len(nums):
                return True
            
            # making subset by adding number in
            for j in range(k):
                if subset[j] + nums[indx] <= subsum:
                    subset[j] += nums[indx]
                    if dfs(indx + 1):
                        return True
                    subset[j] -= nums[indx]
                
                if subset[j] == 0:
                    break
            
            return False
        
        return dfs(0)