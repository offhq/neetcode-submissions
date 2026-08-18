from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        time = 0
        heap = []
        queue = deque([])
        for key, freq in counter.items():
            heapq.heappush(heap, [-freq, key])
        while heap or queue:            
            if heap:
                processed = heapq.heappop(heap)
                processed[0] += 1
                if processed[0] != 0:
                    queue.append([processed, time + n])
            while queue and queue[0][1] <= time:
                reinsert = queue.popleft()
                heapq.heappush(heap, reinsert[0])
            time += 1
            
        return time






        
        