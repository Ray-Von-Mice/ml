class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        for ind, num in enumerate(nums):
            if num > 0:
                break
            if ind > 0 and num == nums[ind - 1]:
                continue 
            
            first = num
            left, right = ind + 1, n - 1
            while left < right:
                three_sum = first + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                 
        return result