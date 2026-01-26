class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(head, end):
            while head < end:
                nums[head], nums[end] = nums[end], nums[head]
                head += 1
                end -= 1
        
        # reverse entire array [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1], k = 3
        reverse(0, n - 1)

        # reverse first k [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
        reverse(0, k - 1)

        # reverse the rest [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
        reverse(k, n - 1)