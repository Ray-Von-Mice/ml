class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def shipable(weightCap) -> bool:
            daysNeed = 1
            tmpCap = weightCap
            for w in weights:
                if tmpCap - w < 0:
                    daysNeed += 1
                    if daysNeed > days:
                        return False
                    # new day, new shipment means full capacity avaliable
                    tmpCap = weightCap
                tmpCap -= w
            return True

        left, right = max(weights), sum(weights)
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            if shipable(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result