class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        all_perms = self.permute(nums[1:])
        
        for perm in all_perms:
            for i in range(len(perm) + 1):
                tmp = perm[:]
                tmp.insert(i, nums[0])
                result.append(tmp)
        
        return result