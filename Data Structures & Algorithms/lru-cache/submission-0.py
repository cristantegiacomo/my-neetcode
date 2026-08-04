class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}    # mp: key -> nodo

        # left contiene LRU, right contiene MRU 
        self.left, self.right = Node(0,0), Node(0,0)  
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next = next.prev = node
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    def get(self, key: int) -> int:
        mp = self.mp
        if key in mp:
            self.remove(mp[key])
            self.insert(mp[key])
            return mp[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        mp = self.mp
        if key in mp:
            self.remove(mp[key])
        mp[key] = Node(key, value)
        self.insert(mp[key])

        lru = self.left.next
        if len(mp) > self.cap:
            del mp[lru.key]
            self.remove(lru)