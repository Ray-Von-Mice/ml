class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 2
        
        cur = 0
        for num in nums:
            if num != nums[cur - 2] or cur < 2:
                nums[cur] = num
                cur += 1
        
        return cur