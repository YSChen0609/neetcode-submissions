"""
use a dll + hashmap to implement
when ever we "access" a key, we move it to the mru (end of the dll), and update the lru ptr

Time: O(1)
Space: O(n)

dict: key->ptr to dll
node class (dll)
ptrs


start -> 1 -> 2 -> 3 -> end
        lru       mru
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.size = 0
        self.start, self.end = Node(-1, 0), Node(-2, 0)
        self.start.next, self.end.prev = self.end, self.start

    def remove(self, node):
        # remove a node
        node.prev.next, node.next.prev = node.next, node.prev
    
    def moveEnd(self, node):
        # move a node to the end of dll
        node.prev, node.next = self.end.prev, self.end
        self.end.prev.next = self.end.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            # move the node to the end
            node = self.cache[key]
            self.remove(node)
            self.moveEnd(node)
        
            return node.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the val of the key
            node = self.cache[key]
            node.val = value
            # move to end
            self.remove(node)
            self.moveEnd(node)
            return

        if self.capacity == self.size:
            # remove the lru
            lru = self.start.next
            self.remove(lru) # aka lru
            self.cache.pop(lru.key)
            self.size -= 1

        # add the new node to end
        cur = Node(key, value)
        self.moveEnd(cur)
        self.cache[key] = cur
        self.size += 1
        
