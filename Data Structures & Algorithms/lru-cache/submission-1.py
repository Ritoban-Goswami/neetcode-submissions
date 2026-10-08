class Node:
    
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add_to_head(self.cache[key])
            return self.cache[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.add_to_head(self.cache[key])
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev    
            self.remove(lru_node)
            del self.cache[lru_node.key]
    
    def add_to_head(self, node: Node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove(self, node: Node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
