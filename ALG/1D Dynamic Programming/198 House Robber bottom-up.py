class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        values = [0] * n
        values[0], values[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            values[i] = max(nums[i] + values[i - 2], values[i - 1])
        
        return values[-1]