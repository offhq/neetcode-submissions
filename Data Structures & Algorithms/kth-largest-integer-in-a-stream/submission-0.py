import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = []
        self.k = k
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        self.heap = heap

        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]


        
