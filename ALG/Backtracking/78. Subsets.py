class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        n = len(nums)
        def dfs(indx):
            if indx >= n:
                res.append(subset[:])
                return
            
            # explore further with nums[index]
            subset.append(nums[indx])
            dfs(indx + 1)
            subset.pop()
            # explore further withOUT nums[index]
            dfs(indx + 1)

        dfs(0)
        return res