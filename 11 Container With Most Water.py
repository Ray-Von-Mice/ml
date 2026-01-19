class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        result = 0
        while left < right:
            # area/water volume is determined by the shorter height 
            area = min(height[left], height[right]) * (right - left)
            result = max(area, result)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return result