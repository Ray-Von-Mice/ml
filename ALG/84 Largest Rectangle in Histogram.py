class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        stack = []
        maxArea = 0
        for index, height in enumerate(heights):
            start_left = index
            while stack and stack[-1][1] > height:
                left, leftHeight = stack.pop()
                maxArea = max(maxArea, (index - left) * leftHeight)
                start_left = left
            stack.append((start_left, height))

        for index, height in stack:
            maxArea = max(maxArea, (n - index) * height)
        
        return maxArea