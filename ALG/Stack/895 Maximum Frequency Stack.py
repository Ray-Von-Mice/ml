class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.num_freq = defaultdict(int) # 2 appears 3 times -> ('2' - 3)
        self.freqT_nums = defaultdict(list) # 2, 5 appears 3 times -> (3 - [2, 5], 2- [2, 5], 1 - [2, 5])

    def push(self, val: int) -> None:
        self.num_freq[val] += 1
        self.maxFreq = max(self.maxFreq, max(self.num_freq.values()))
        self.freqT_nums[self.num_freq[val]].append(val)

    def pop(self) -> int:
        res = self.freqT_nums[self.maxFreq].pop()
        if not self.freqT_nums[self.maxFreq]:
            self.maxFreq -= 1
        self.num_freq[res] -= 1
        
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()