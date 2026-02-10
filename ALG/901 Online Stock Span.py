class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        default = 1
        while self.stack and price >= self.stack[-1][0]:
            default += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, default))
        return default


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)