class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] < target else 1
        
        left, mixArr = 0, float("inf")
        currSum = 0
        for i in range(n):
            currSum += nums[i]
            if currSum >= target:
                while currSum >= target:
                    mixArr = min(mixArr, i - left + 1)
                    currSum -= nums[left]
                    left += 1
        
        return 0 if mixArr == float("inf") else mixArr