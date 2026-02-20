class Node:

    def __init__(self, prev, nxt, key: int, val: int):
        self.prev = prev
        self.nxt = nxt
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {} # key: key - value: node
        self.head = Node(None, None, -2, -2)
        self.tail = Node(None, None, -2, -2)
        self.limit = capacity

        # head next will be LRU, tail prev will be MRU
        self.head.nxt, self.tail.prev = self.tail, self.head
    
    def remove(self, node) -> None:
        prev_node, nxt_node = node.prev, node.nxt
        node.nxt, node.prev = None, None
        prev_node.nxt = nxt_node
        nxt_node.prev = prev_node

    def insert(self, node) -> None:
        # always insert at the end of linked list
        prev_node = self.tail.prev
        prev_node.nxt = node
        self.tail.prev = node
        node.prev = prev_node
        node.nxt = self.tail


    def get(self, key: int) -> int:
        if key in self.mp:
            # remove from the linked list, re-insert it at the end
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        
        # insert/re-insert at the end
        insertion = Node(None, None, key, value)
        self.insert(insertion)
        self.mp[key] = insertion

        # check limit and pop LRU
        if len(self.mp) > self.limit:
            lru = self.head.nxt
            self.remove(lru)
            del self.mp[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)