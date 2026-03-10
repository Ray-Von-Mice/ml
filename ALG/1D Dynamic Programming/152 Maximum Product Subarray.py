class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # curMin for encoutering negative number, curMin * negative -> new curMax
        curMax, curMin = 1, 1
        result = max(nums) # for [-2, 0, -1]
        for num in nums:
            if num == 0:
                curMax, curMin = 1, 1
                continue
            tmp = curMax # tmp value store curMax before recompute it
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num * tmp, num * curMin, num)
            result = max(curMax, curMin, result)
            print((curMax, curMin, result))

        return result