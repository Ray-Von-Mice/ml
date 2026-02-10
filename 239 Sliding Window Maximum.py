class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1 or k == 1:
            return nums
        left, right = 0, 0
        res = []
        # monotonically decrease, if nums[cur] > nums[window.top], keep pop window.
        window = deque()

        while right < n:
            # only smaller element will be added
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            window.append(right)

            # window has shifted left, pop the left most index stored
            if left > window[0]:
                window.popleft()
            
            # shift left only when window size is greater than or equals to k, to maintain k
            if (right + 1) >= k:
                left += 1
                res.append(nums[window[0]])

            right += 1
        
        return res