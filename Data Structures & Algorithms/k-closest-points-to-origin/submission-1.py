import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:

            dist = -(x**2 + y**2)
            heapq.heappush(heap, (dist, [x, y]))
            
            # If heap exceeds size k, remove the farthest point
            if len(heap) > k:
                heapq.heappop(heap)



        return [i[1] for i in heap]
        
        