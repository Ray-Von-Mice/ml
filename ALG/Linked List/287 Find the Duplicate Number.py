class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        # find interception or junction, prove cycle exist
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        '''
            N*slow = fast -> N(P + C - X) = P + NC - X -> (N-1)P = (N-1)X -> P = X
            P: distance to cycle
            X: distance from interception of fast and slow ptrs, to the converge ptr (duplicate)
        '''
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow