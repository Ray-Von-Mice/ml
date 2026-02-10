class MinStack:

    def __init__(self):
        self.lt = []
        self.minlt = []

    def push(self, val: int) -> None:
        self.lt.append(val)
        min_val = float("inf")
        if self.minlt:
            min_val = min(val, self.minlt[-1])
        else:
            min_val = min(min_val, val)
        self.minlt.append(min_val)
        

    def pop(self) -> None:
        self.lt.pop()
        self.minlt.pop()

    def top(self) -> int:
        return self.lt[-1]

    def getMin(self) -> int:
        return self.minlt[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()