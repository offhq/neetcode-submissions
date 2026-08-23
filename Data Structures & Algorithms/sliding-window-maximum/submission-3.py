import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res = [- heap[0][0]]
        left = 0
        right = k
        while right < len(nums):
            heapq.heappush(heap, (-nums[right], right))
            while heap and heap[0][1] <= left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            left += 1
            right += 1
        return res


        