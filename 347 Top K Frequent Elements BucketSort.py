class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        freq_l = [[] for _ in range(n+1)]
        for num, count in freq.items():
            freq_l[count].append(num)
        
        result = []
        sl = len(freq_l)
        for i in range(sl - 1, 0, -1):
            for number in freq_l[i]:
                result.append(number)
                if len(result) == k:
                    return result