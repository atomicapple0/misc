from collections import deque

class Node():
    def __init__(self):
        super().__init__()
        self.prev = None
        self.val = None
        self.next = None

class DequeEfficient():
    def __init__(self):
        super().__init__()
        self.front = None
        self.back = None
        self.mapping = {}
        self.size = 0
    
    def append(self, page):
        self.size += 1
        new_node = Node()
        new_node.val = page
        self.mapping[page] = new_node
        if self.front == None:
            self.front = new_node
            self.back = self.front
            return
        old_front = self.front
        self.front = new_node
        self.front.prev = old_front
        old_front.next = self.front
    
    def popleft(self):
        self.size -= 1
        del self.mapping[self.back.val]
        self.back = self.back.next

    def remove(self, page):
        self.size -= 1
        curr = self.mapping[page]
        del self.mapping[page]
        if self.front == curr and self.back == curr:
            self.front = None
            self.back = None
            return
        if self.front == curr:
            self.front = curr.prev
            return
        if self.back == curr:
            self.back = curr.next
            return
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    
    def __repr__(self):
        return str(self.mapping) + str(self.back) + str(self.front)


def lruCacheMisses(num, pages, maxCacheSize):
    deq = DequeEfficient()
    miss = 0
    for page in pages:
        if page in deq.mapping.keys():
            deq.remove(page)
            deq.append(page)
        else:
            miss += 1
            if deq.size == maxCacheSize:
                deq.popleft()
            deq.append(page)
    return miss


print(lruCacheMisses(6, [1,2,1,3,1,2], 2))