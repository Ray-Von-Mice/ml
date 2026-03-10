class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        counter = [1] * n
        '''
            arr: [1, 3, 5, 2, 4]
            LIS[4] = 1, LIS[3] = 1 + LIS[4], LIS[2] = 1 + LIS[3] (if cur < arr[3]) or 1 + LIS[4] (if cur < arr[4]) or 1 ...
        '''
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    counter[i] = max(counter[i], 1 + counter[j])
        
        return max(counter)