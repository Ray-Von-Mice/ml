class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.sz = 0
        self.limit = k
        self.head = 0
        self.tail = -1 # in order for circular behavior, tail points to the last element of array

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.limit # ensure circular without expanding the array
        self.arr[self.tail] = value
        self.sz += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.limit
        self.sz -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        return True if self.sz == 0 else False

    def isFull(self) -> bool:
        return True if self.sz == self.limit else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()