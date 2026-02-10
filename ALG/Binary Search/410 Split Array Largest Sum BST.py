class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitAble(largestSum):
            subArryNum = 0
            currSum = 0
            for i in nums:
                currSum += i
                '''
                current sum greater than largestSum, split by increasing sub array count 
                and set current sum to i (create new sub array started from i)
                '''
                if currSum > largestSum:
                    subArryNum += 1
                    currSum = i
            
            return subArryNum + 1 <= k
        
        left, right = max(nums), sum(nums)
        result = 0
        while left <= right:
            mid = left + (right - left) // 2
            # splitable, looking for smaller largest sum
            if splitAble(mid):
                result = mid
                right = mid - 1
            # not splitable, looking for larger largest sum
            else:
                left = mid + 1
        
        return result