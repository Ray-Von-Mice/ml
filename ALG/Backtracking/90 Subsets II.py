class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        n = len(nums)
        nums.sort()
        def dfs(indx):
            if indx >= n:
                result.append(subset[:])
                return
            subset.append(nums[indx])
            dfs(indx + 1)
            subset.pop()
            while indx + 1 < n and nums[indx] == nums[indx + 1]:
                indx += 1
            dfs(indx + 1)
        dfs(0)
        return result