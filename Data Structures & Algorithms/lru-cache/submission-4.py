class ListNode:
    def __init__(self, val= 0 , next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key = {}
        self.dummy = ListNode(0)
        self.end = self.dummy
        
    def get(self, key: int) -> int:
        if key in self.key:
            node = self.key[key][0]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev

                node.prev = self.end
                self.end.next = node
                self.end = node
                self.end.next = None
            return self.key[key][1]

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key:
            node = ListNode(key, None, self.end)
            self.end.next = node
            self.end = node
            self.key[key] = (node, value)
            if len(self.key) > self.capacity:
                removal = self.dummy.next
                self.dummy.next = removal.next
                if removal.next:
                    removal.next.prev = self.dummy
                self.key.pop(removal.val)
                if self.dummy.next is None:
                    self.end = self.dummy
        else:
            node = self.key[key][0]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev

                node.prev = self.end
                self.end.next = node
                self.end = node
                self.end.next = None
            self.key[key] = (node, value)


            
        
        



        
