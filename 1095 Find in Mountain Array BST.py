# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        # find peak in (1, len - 2) since guaranteed peak_index locates 0 < peak < length - 1
        l, r = 1, n - 2
        peak = 0
        while l <= r:
            m = l + (r - l) // 2
            l_value, mid_value, r_value = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if l_value > mid_value > r_value:
                r = m - 1
            elif l_value < mid_value < r_value:
                l = m + 1
            else:
                peak = m
                break

        # BST in left portion, increasing order
        l, r = 0, peak
        while l <= r:
            m = l + (r - l) // 2
            m_value =  mountainArr.get(m)
            if m_value < target:
                l = m + 1
            elif m_value > target:
                r = m - 1
            else:
                return m
        
        # BST in right portion, decreasing order
        l, r = peak, n - 1
        while l <= r:
            m = l + (r - l) // 2
            m_value =  mountainArr.get(m)
            if m_value < target:
                r = m - 1
            elif m_value > target:
                l = m + 1
            else:
                return m

        return -1