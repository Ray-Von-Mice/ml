class Node:

    def __init__(self, prev, nxt, key: int, val: int, cntr: int):
        self.prev, self.nxt = prev, nxt
        self.key, self.val, self.cntr = key, val, cntr

class DLinkedList:

    def __init__(self):
        self.head = Node(None, None, -1. -1, -1, -1)
        self.tail = Node(None, None, -1. -1, -1, -1)
        self.head.nxt, self.tail.prev = self.tail, self.head
        self.mp = {} # key: key, value: node
    
    def size(self) -> int:
        return len(self.mp)
    
    def insert(self, key, value, cnter) -> None: # always insert at the end
        node = Node(None, None, key, value, cnter)
        prev_node = self.tail.prev
        prev_node.nxt, self.tail.prev = node, node
        node.prev, node.nxt = prev_node, self.tail
        self.mp[node.key] = node
    
    def remove(self, key: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            prev_node, nxt_node = node.prev, node.nxt
            node.prev, node.nxt = None, None
            prev_node.nxt, nxt_node.prev = nxt_node, prev_node
            del self.mp[node.key]

    def popLeft(self) -> Node:
        del_node = self.head.nxt
        nxt_node = self.head.nxt.nxt
        del_node.prev, del_node.nxt = None, None
        self.head.nxt = nxt_node
        nxt_node.prev = self.head
        del self.mp[del_node.key]
        return del_node

class LFUCache:

    def __init__(self, capacity: int):
        self.cnter_mp = defaultdict(int) # key: key, value: counter of the key
        self.value_mp = defaultdict(int) # key: key, value: value
        self.cnt_lk_mp = defaultdict(DLinkedList) # key: user counter, value: linked list of nodes with same counter
        self.limit = capacity
        self.lruCnter = 0

    def updateCounter(self, key: int, value: int):
        n = self.cnter_mp[key]
        # update counter map
        self.cnter_mp[key] += 1
        # remove from old counter linkedlist, insert into new, update cnt_lk_mp
        self.cnt_lk_mp[n].remove(key)
        self.cnt_lk_mp[n + 1].insert(key, value, n)

        # if old counter happens to be lru, and lru Linkedlist is emtpy, need new lru
        if n == self.lruCnter and self.cnt_lk_mp[n].size() == 0:
            self.lruCnter += 1

    def get(self, key: int) -> int:
        if key not in self.value_mp:
            return -1
        value = self.value_mp[key]
        self.updateCounter(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        # remove LRU if limit has been reached, pop LRU from all
        if key not in self.value_mp and len(self.value_mp) == self.limit:
            lru = self.cnt_lk_mp[self.lruCnter].popLeft()
            del self.cnter_mp[lru.key]
            del self.value_mp[lru.key]
        # new key
        self.value_mp[key] = value
        self.updateCounter(key, value)
        self.lruCnter = min(self.lruCnter, self.cnter_mp[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)