class Node:

    def __init__(self, val, nxt, prev):
        self.val, self.nxt, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        self.sz = 0
        self.head = Node(-1, None, None)
        self.tail = Node(-1, None, None)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = self.head
        while curr:
            if curr.nxt == self.tail:
                break
            curr = curr.nxt
        insert = Node(value, self.tail, curr)
        curr.nxt = insert
        self.tail.prev = insert
        self.sz += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        past = self.head.nxt.nxt
        delete = self.head.nxt
        delete.nxt = None
        delete.prev = None
        self.head.nxt = past
        past.prev = self.head
        self.sz -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.sz == 0

    def isFull(self) -> bool:
        return self.sz == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()