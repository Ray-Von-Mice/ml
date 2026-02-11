class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left, right = 0, n - 1
        result = 0
        max_left, max_right = height[left], height[right]

        while left < right:
            if height[left] > height[right]:
                right -= 1
                max_right = max(height[right], max_right)
                result += (max_right - height[right])
            else:
                left += 1
                max_left = max(height[left], max_left)
                result += (max_left - height[left])
        
        return result