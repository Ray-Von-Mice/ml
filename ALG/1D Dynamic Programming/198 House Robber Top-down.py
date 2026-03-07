class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        arr = [-1] * n
        # 40, 1, 1, 1, 1, 40
        def traverse(indx):
            if indx >= len(nums):
                return 0
            
            if arr[indx] != -1:
                return arr[indx]
            
            # rob current indx and (indx + 2) value or skip current
            arr[indx] = max(nums[indx] + traverse(indx + 2), traverse(indx + 1))
            return arr[indx]
        
        return traverse(0)