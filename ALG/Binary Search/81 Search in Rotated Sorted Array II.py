class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return nums[0] == target
        
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # real start element in the left portion
            if nums[left] < nums[mid]: 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # real start element in the right portion
            elif nums[left] > nums[mid]: 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # duplicate, simply move left pointer
                left += 1

        return False