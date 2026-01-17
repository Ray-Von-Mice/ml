class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my product = my prefix prod * my suffix prod -> prod[i] = pref[i] * suffx[i]
        n = len(nums)
        result = [1] * n
        pref, suffx = 1, 1
        for i in range(n):
            result[i] = pref
            pref *= nums[i]
        
        for j in range(n-1, -1, -1):
            result[j] *= suffx
            suffx *= nums[j]
        
        return result