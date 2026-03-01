class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(indx, total):
            if indx == len(nums):
                return total
            
            inres = dfs(indx + 1, total ^ nums[indx])
            exres = dfs(indx + 1, total)

            return inres + exres
        
        return dfs(0, 0)