from collections import deque
def lruCacheMisses(num, pages, maxCacheSize):
    deq = deque()
    miss = 0
    for page in pages:
        if page in deq:
            deq.remove(page)
            deq.append(page)
        else:
            miss += 1
            if len(deq) == maxCacheSize:
                deq.popleft()
            deq.append(page)
    return miss


print(lruCacheMisses(6, [1,2,1,3,1,2], 2))