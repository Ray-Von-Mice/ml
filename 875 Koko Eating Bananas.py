class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            mid = l + (r - l) // 2 # mid is the speed of eating
            time = 0

            for pile in piles:
                time += math.ceil(float(pile) / mid)
            
            if time > h:
                l = mid + 1
            else:
                result = mid
                r = mid - 1
        
        return result