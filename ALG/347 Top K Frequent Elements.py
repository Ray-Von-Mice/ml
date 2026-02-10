class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        freq = {}
        for num in nums:
            try:
                freq[num]
            except KeyError:
                freq[num] = 0
            freq[num] += 1
        
        tmp = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(tmp[i][0])

        return result