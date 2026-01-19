class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        numSet = set(nums)
        result = 0

        for num in numSet:
            # find the head of the sequence by locating its "not exist" num - 1
            if (num - 1) not in numSet:
                steps = 1
                while (num + steps) in numSet:
                    steps += 1
                result = max(steps, result)
        return result