import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        lookup = {}
        for point in points:
            x = point[0]
            y = point[1]
            distance_sqrd = -(x**2 + y**2)
            if distance_sqrd not in lookup:
                lookup[distance_sqrd] = []

            lookup[distance_sqrd].append(point)
            if len(heap) == k:
                remove = heapq.heappushpop(heap, distance_sqrd)
                lookup[remove].pop()
                if not lookup[remove]:
                    del lookup[remove]
            else:
                heapq.heappush(heap, distance_sqrd)
        res = []
        for i in lookup.values():
            for x in i:
                res.append(x)

        return res
        
        