class Solution:
    def calculate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        arr = [0] * n
        arr[0], arr[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
        return arr[-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # max value from nums 1 to n - 1
        value1 = self.calculate(nums[1:])
        # max value from nums 0 to n - 2
        value2 = self.calculate(nums[:n - 1])

        return max(value1, value2)