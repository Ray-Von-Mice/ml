class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n == 1:
            return arr
        
        def closer(a, b, x) -> int:
            if (abs(a - x) < abs(b - x)) or (abs(a - x) == abs(b - x) and a < b):
                return a
            else:
                return b
        
        left, right = 0, n - 1
        while right - left >= k:
            cand = closer(arr[left], arr[right], x)
            # if left is closer, chop right off by 1; vice versa
            if cand == arr[left]:
                right -= 1
            else:
                left += 1

        return arr[left:right + 1]