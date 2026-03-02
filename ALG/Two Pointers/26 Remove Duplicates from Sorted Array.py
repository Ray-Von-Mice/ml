class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0 #index that diff number is being coping to
        for num in nums:
            if num != nums[cur - 1] or cur < 1:
                nums[cur] = num
                cur += 1
        
        return cur