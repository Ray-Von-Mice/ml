class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        # find smaller array
        if n < m:
            SA, LA = nums1, nums2
        else:
            SA, LA = nums2, nums1
        totalnums = n + m
        halfnums = totalnums // 2

        left, right = 0, len(SA) - 1
        while 1:
            mid_SA = left + (right - left) // 2
            # looking for numbers of elements, NOT index
            mid_LA = halfnums - mid_SA - 2

            SA_left = SA[mid_SA] if mid_SA >= 0 else float('-inf')
            SA_right = SA[mid_SA + 1] if mid_SA + 1 < len(SA) else float('inf')
            LA_left = LA[mid_LA] if mid_LA >= 0 else float('-inf')
            LA_right = LA[mid_LA + 1] if mid_LA + 1 < len(LA) else float('inf')

            # partition achieved
            if SA_left <= LA_right and LA_left <= SA_right:
                # odd numbers of elements
                if totalnums % 2:
                    return min(SA_right, LA_right)
                # even
                return (min(SA_right, LA_right) + max(SA_left, LA_left)) / 2
            elif SA_left > LA_right:
                right = mid_SA - 1
            else:
                left = mid_SA + 1